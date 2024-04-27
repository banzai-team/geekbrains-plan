import argparse
import json
import os

import requests


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='VacancyCollection',
                    description='Saves lister in *input file* vacancies from hh.ru into *output file*')
    
    parser.add_argument('-i', '--input', default="input.json")   
    parser.add_argument('-o,', '--output', default="ouput.json")   

    args = parser.parse_args()


    in_file = args.input
    out_file = args.output

    cfg = {}

    with open(in_file) as file:
        cfg = json.load(file)
    
    BASE_URL = "https://api.hh.ru/vacancies"

    result = {
        "total": 0,
        "vacancies": []
    }

    for vanancy in cfg["vacancies"]:
        
        for page in range(0, cfg["pages_per_vacancy"]):
            params = {
                "text": vanancy,
                "page": page,
                "per_page": cfg["per_page"]
            }
            r = requests.get(url = BASE_URL, params = params)
            data = r.json()

            
        print(data["items"][0])
