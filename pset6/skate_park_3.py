
import json

def check_age_experience(skaters):
    for skater in skaters:
        name = skater["name"]
        age = skater["age"]
        is_experienced = skater["is_experienced"]

        if age >= 13 and is_experienced:
            print(f"Hi {name}, welcome to the skate park!")

try:
    with open("skaters.json", "r") as file:
        skaters = json.load(file)

    check_age_experience(skaters)

except FileNotFoundError:
    print("Error: skaters.json was not found.")
