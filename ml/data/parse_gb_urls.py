import json
import trafilatura

with open('edu_programs.json') as f:
    program2url = json.load(f)
program2url = {k: v['url'] for k, v in program2url.items()}

program2url_text = {}
for program_id, url in program2url.items():
    print(program_id, url)
    downloaded = trafilatura.fetch_url(url)
    program2url_text[program_id] = trafilatura.extract(downloaded)

with open('gb_program2url_texts.json', 'w') as f:
    json.dump(program2url_text, f)
