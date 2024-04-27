import json
from pathlib import Path

import yaml

_ROOT_ML_DIR = Path(__file__).parent.parent.parent.absolute()
_DATA_DIR = _ROOT_ML_DIR / 'data'

with open(_DATA_DIR / 'courses.yaml', 'r') as f:
    COURSES_GROUPED = yaml.safe_load(f)

# todo: two stage filtering
with open(_DATA_DIR / 'llm_simular_matches.json', 'r') as f:
    SIMULAR_COURSES = json.load(f)

with open(_DATA_DIR / 'skills_from_llm.json', 'r') as f:
    PROGRAM_SKILLS = json.load(f)

with open(_DATA_DIR / 'edu_programs.json', 'r') as f:
    EDU_PROGRAMS = json.load(f)
