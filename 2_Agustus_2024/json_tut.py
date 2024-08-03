import json

with open('data.json', 'r') as file:
    data = file.read()
    
print(data, type(data))
print(data['members'])

todos = {"todos" : ["eat", "sleep", "code"]}

with open('data2.json', 'w') as file:
    json.dump(todos, file)
    
with open('data2.json', 'r') as file:
    data = json.load(file)
    
print(data['todos'][3])