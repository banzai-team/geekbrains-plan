
import asyncio
import json
from db import prisma

if __name__ == "__main__":

    programs_file = 'programs.json'
    modules_file = 'modules.json'
    prices_file = 'calculate.json'

    
    res = prisma.prisma_client.connect()

    programs = {}
    modules = {}
    quarters = {}
    prices = {}

    with open(programs_file) as file:
        programs = json.load(file)

    with open(modules_file) as file:
        modules_pre = json.load(file)
        for (program_id, module_pre) in modules_pre.items():
            modules[program_id] = {}
            if "modules" in  module_pre["plan_edu"]:
                modules[program_id] = module_pre["plan_edu"]["modules"]
            if "quarters" in  module_pre["plan_edu"]:
                quarters[program_id] = module_pre["plan_edu"]["quarters"]

    with open(prices_file) as file:
        prices_pre = json.load(file)
        for price_pre in prices_pre["prices"]:
            program_id = price_pre["productId"]
            program_price = None
            for price_pre_option in price_pre["prices"]:
                if price_pre_option["type"] == "price":
                    program_price = price_pre_option["value"]
                    break
            prices[program_id] = {
                "program_price": program_price,
                "days_amount": price_pre["daysAmount"]
            }

    for program_id, program in programs.items():
        to_save = {
            "id": int(program_id),
            "name": program["name"],
            "tag": program["Направление (тег)"],
            "speciality": program["Специализация"],
            "url": program["url"],
            "difficulty": program["Уровень сложности"]
        }

        if program_id in prices:
            to_save["price"] = prices[program_id]["program_price"]
            to_save["days_amount"] = prices[program_id]["days_amount"]

        res = prisma.prisma_client.program.create(to_save)
        if program_id in modules:
            for i, module in enumerate(modules[program_id]):
                quarter_to_save = {
                    "title": module["title"], 
                    "ordinal": i, "program": {
                    "connect": {
                        "id": int(program_id)
                    }
                }} 
                res = prisma.prisma_client.module.create(quarter_to_save)
                
        if program_id in quarters:
            for i, quarter in enumerate(quarters[program_id]):
                quarter_to_save = {
                    "title": quarter["title"], 
                    "ordinal": i, "program": {
                    "connect": {
                        "id": int(program_id)
                    }
                }} 
                res = prisma.prisma_client.quarter.create(quarter_to_save)

    prisma.prisma_client.disconnect()
    print('saved')

        


    

        