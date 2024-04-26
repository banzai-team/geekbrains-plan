from guidance import models, select, gen
import guidance
import re

import transformers
import torch

from .dict import courses_grouped

import yaml
from app.config import device

data = yaml.safe_load(courses_grouped)

model_name_or_path = "NousResearch/Meta-Llama-3-8B-Instruct"
# model_name_or_path = "NousResearch/Meta-Llama-3-70B-Instruct"
lm = models.Transformers(
    model_name_or_path,
    device_map="auto",
    load_in_8bit=True,
    _attn_implementation='sdpa'
)

pipeline = transformers.pipeline(
    "text-generation",
    model=model_name_or_path,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device=device,
)


def narrow(header: str, sample_text: str):
    messages = [
        {"role": "system",
         "content": "Ты очень полезный ассистен, который помогает подбирать кадры для IT компании и не только"},
        {"role": "user",
         "content": f"Вот название и описание вакансии\n<header>{header}</header><text>{sample_text}</text>"},
        {"role": "assistant", "content": f"Я готов отвечать на вопросы"},
    ]
    assistant_eos = '<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n'
    user_eos = '<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n'

    prompt = pipeline.tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    prompt = prompt[:-len(assistant_eos)]
    prompt += user_eos
    level_d = data['children']
    level_idx = 0
    output = lm + prompt
    result_edu_course = None

    while True:

        message = ""
        message = f"Напиши номер категории, к которой вакансия относится больше всего:\n"
        for i in range(1, len(level_d) + 1):
            message += f'{i}. ' + level_d[i - 1]['name']
            #         if level_d[i].get('add_desc'):
            #             lm += level_d[i]['desc']
            message += '\n'

        output += message + assistant_eos
        output += select([i for i in range(1, len(level_d) + 1)], name=f'level_{level_idx}') + user_eos

        choosen_index = int(output[f'level_{level_idx}']) - 1

        #     if
        if not level_d[choosen_index].get('children'):
            result_edu_course = level_d[choosen_index]['name']
            break

        level_d = level_d[choosen_index].get('children')
        level_idx += 1

    return result_edu_course
