import json

with open('todos.json', 'r') as file:
    data = json.load(file)
    
print(data, type(data))