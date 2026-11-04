
import json

with open("ramps.json", "r") as file:
    ramps = json.load(file)

for k, v in ramps.items():
    print(f"{k}s favorite ramp is {v}")
