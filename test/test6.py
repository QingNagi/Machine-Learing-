import json

number = [2, 3, 4, 5]

filename = 'numbers.json'
with open(filename, 'r+') as file:
    json.dump(number, file)

with open(filename) as file:
    a = json.load(file)
    print(a)