from typing import Dict, List, Any

import torch
import transformers
import yaml
from guidance import models, select

from app.config import device, MODEL_PATH
from .dicts import COURSES_GROUPED, SIMULAR_COURSES, PROGRAM_SKILLS, EDU_PROGRAMS


model_name_or_path = "NousResearch/Meta-Llama-3-8B-Instruct"
# model_name_or_path = "NousResearch/Meta-Llama-3-70B-Instruct"
n_gpu_layers = 1  # Metal set to 1 is enough.
n_batch = 512
N_CTX = 4096

lm = models.LlamaCpp(
    MODEL_PATH,
    n_gpu_layers=n_gpu_layers,
    n_ctx=N_CTX,
    n_batch=n_batch
)
MIN_RATING = 1
MAX_RATING = 9

ASSISTANT_EOS = '<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n'
USER_EOS = '<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n'

tokenizer = transformers.AutoTokenizer.from_pretrained(
    model_name_or_path,
)


def narrow(sample_text: str) -> dict[str, list[Any] | Any]:
    sample_text = sample_text[:2*N_CTX]
    messages = [
        {"role": "system",
         "content": "Ты очень полезный ассистент, который помогает подбирать кадры для IT компании и не только"},
        {"role": "user", "content": (
            f"Вот описание вакансии на которую нужно подобрать ближайший учебный курс:\n<text>{sample_text}</text>.\n"
            "Предупреждаю, что не ко всем вакансиям можно подобрать обучающий курс."
        )},
        {"role": "assistant", "content": f"Я готов отвечать на вопросы по переданной вакансии"},
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    prompt = prompt[:-len(ASSISTANT_EOS)]
    prompt += USER_EOS
    level_d = COURSES_GROUPED['children']
    level_idx = 0

    base_output = lm + prompt
    output = base_output

    course_coverage = None
    skills_need = []
    edu_courses = []

    while True:
        message = f"Напиши номер категории, к которой вакансия относится больше всего:\n"
        for i in range(1, len(level_d) + 1):
            message += f'{i}. ' + level_d[i - 1]['name']
            message += '\n'

        output += message + ASSISTANT_EOS
        output += select([i for i in range(1, len(level_d) + 1)], name=f'level_{level_idx}') + USER_EOS

        choosen_index = int(output[f'level_{level_idx}']) - 1

        if level_d[choosen_index].get('exit'):
            result_edu_course = None
            break

        if not level_d[choosen_index].get('children'):
            result_edu_course = level_d[choosen_index]
            break

        level_d = level_d[choosen_index].get('children')
        level_idx += 1

    if result_edu_course is not None:
        edu_courses += [result_edu_course['id']]
        # is manager
        output += ('Напиши мне "2", если вакансия включает в '
                   'себя управление людьми и "1", если не включает.'
                   ) + ASSISTANT_EOS
        output += select([i for i in range(1, 3)], name=f'is_manager_work') + USER_EOS
        is_manager_work = int(output[f'is_manager_work']) - 1

        # # check skills
        result_edu_course_skills = PROGRAM_SKILLS[str(result_edu_course['id'])]
        skills_output = base_output
        message = (
            f"Насколько целевой вакансии требуются навыки ниже из курса '{result_edu_course['name']}'? "
            f"Напиши номер категории для каждого пункта ниже после запятой. "
            f"Категории:  \"1\" - навык не требуется; \"2\" - навык будет полезен; \"3\" - навык необходим."
            "\n\n"""
        )
        for i in range(1, len(result_edu_course_skills) + 1):
            message += f'{i}. "{result_edu_course_skills[i - 1]["name"]}", '
            message += select(["1", "2", "3"], name=f'skill_{i - 1}')
            message += '\n'

        skills_output += message + USER_EOS

        # # course coverage
        skills_output += (
            f"Можно ли сразу после курса приступать к работе по профессии в вакансии? "
            f"Напиши цифру от {MIN_RATING} (курс не поможет в изучении профессии) "
            f"до {MAX_RATING} (после курса можно сразу приступать к работе)."
        ) + ASSISTANT_EOS
        skills_output += select([i for i in range(MIN_RATING, MAX_RATING + 1)],
                                      name=f'course_coverage') + USER_EOS

        if is_manager_work and result_edu_course['id'] not in ('7918', '7916'):
            # project manager
            edu_courses += ['7916']

        for i in range(len(result_edu_course_skills)):
            skills_need += [{
                'name': result_edu_course_skills[i]['name'],
                'requirement': int(skills_output[f'skill_{i}']) - 2,
            }]
        course_coverage = int(skills_output['course_coverage']) / MAX_RATING

    simular_courses = []
    if s := SIMULAR_COURSES.get(result_edu_course['id']):
        simular_courses = s['simular']

    return {
        'simular_courses': simular_courses,
        'edu_courses': edu_courses,
        'course_coverage': course_coverage,
        'skills_need': skills_need,
    }
