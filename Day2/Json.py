import json

data = {
    "name": "rupesh",
    "age": 20,
    "skills":["python","java"]
}

with open("data.json","w") as f:
    json.dump(data,f,indent=4)