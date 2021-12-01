from collections import defaultdict
from queue import Queue
from math import ceil
def build_ingredient(string):
    parts = string.split(" ")
    return {"ingredient": parts[1], "amount": int(parts[0])}
def build_recipes(data):
    recipes = {}
    for line in data:
        input_str, output_str = line.split(" => ")
        
        ingredients = []
        for ingredient_str in input_str.split(', '):
            ingredients.append(build_ingredient(ingredient_str))
            
        output = build_ingredient(output_str)
        
        recipes[output["ingredient"]] = {
            "servings": output["amount"],
            "ingredients": ingredients
        }
    return recipes

def make_fuel(amount, recipes):
    supply = defaultdict(int)
    orders = Queue()
    orders.put({"ingredient": "FUEL", "amount": amount})
    ore_needed = 0

    while not orders.empty():
        order = orders.get()
        # print(order["ingredient"])
        if order["ingredient"] == "ORE":
            ore_needed += order["amount"]
        elif order["amount"] <= supply[order["ingredient"]]:
            supply[order["ingredient"]] -= order["amount"]
        else:
            print(supply[order["ingredient"]])
            amount_needed = order["amount"] - supply[order["ingredient"]]
            recipe = recipes[order["ingredient"]]
            batches = ceil(amount_needed / recipe["servings"])

            for ingredient in recipe["ingredients"]:
                orders.put({"ingredient": ingredient["ingredient"], "amount": ingredient["amount"] * batches})
            leftover_amount = batches * recipe["servings"] - amount_needed
            supply[order["ingredient"]] = leftover_amount
            print(supply)
    return ore_needed

data = [
    "10 ORE => 10 A",
    "1 ORE => 1 B",
    "7 A, 1 B => 1 C",
    "7 A, 1 C => 1 D",
    "7 A, 1 D => 1 E",
    "7 A, 1 E => 1 FUEL",
]
# data = [
#     "157 ORE => 5 NZVS",
#     "165 ORE => 6 DCFZ",
#     "44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL",
#     "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ",
#     "179 ORE => 7 PSHF",
#     "177 ORE => 5 HKGWZ",
#     "7 DCFZ, 7 PSHF => 2 XJWVT",
#     "165 ORE => 2 GPVTF",
#     "3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT",
# ]

recipes = build_recipes(data)
# for recipe in recipes:
#     print(recipe, recipes[recipe])



print(make_fuel(1, recipes))