from typing import Dict, List, Any

import torch
import transformers
import yaml
from guidance import models, select

from app.config import device, MODEL_PATH
from .dicts import courses_grouped, SIMULAR_COURSES

data = yaml.safe_load(courses_grouped)

model_name_or_path = "NousResearch/Meta-Llama-3-8B-Instruct"
# model_name_or_path = "NousResearch/Meta-Llama-3-70B-Instruct"
n_gpu_layers = 1  # Metal set to 1 is enough.
n_batch = 2048
lm = models.LlamaCpp(MODEL_PATH,
                     n_gpu_layers=n_gpu_layers,
                     n_ctx=4096,
                     n_batch=n_batch
                     )

tokenizer = transformers.AutoTokenizer.from_pretrained(
    model_name_or_path,
)


def narrow(header: str, sample_text: str) -> dict[str, list[Any] | Any]:
    messages = [
        {"role": "system",
         "content": "Ты очень полезный ассистен, который помогает подбирать кадры для IT компании и не только"},
        {"role": "user",
         "content": f"Вот название и описание вакансии\n<header>{header}</header><text>{sample_text}</text>"},
        {"role": "assistant", "content": f"Я готов отвечать на вопросы"},
    ]
    assistant_eos = '<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n'
    user_eos = '<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n'

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    prompt = prompt[:-len(assistant_eos)]
    prompt += user_eos
    level_d = data['children']
    level_idx = 0
    output = lm + prompt

    while True:
        message = f"Напиши номер категории, к которой вакансия относится больше всего:\n"
        for i in range(1, len(level_d) + 1):
            message += f'{i}. ' + level_d[i - 1]['name']
            #         if level_d[i].get('add_desc'):
            #             lm += level_d[i]['desc']
            message += '\n'

        output += message + assistant_eos
        output += select([i for i in range(1, len(level_d) + 1)], name=f'level_{level_idx}') + user_eos

        choosen_index = int(output[f'level_{level_idx}']) - 1

        if not level_d[choosen_index].get('children'):
            result_edu_course = level_d[choosen_index]['id']
            break

        level_d = level_d[choosen_index].get('children')
        level_idx += 1

    print(result_edu_course)

    sm = SIMULAR_COURSES.get(result_edu_course, {}).get('simular', [])

    return {
        'simular_courses': sm,
        'edu_courses': [int(result_edu_course)]
    }
