# JSON

student = {
    "name": "Salih",
    "course": "Python",
    "age": 23
}
import json

data=json.dumps(student)
print(data)
print(type(data))

text = '{"company":"OpenAI","role":"AI Engineer"}'
dictText=json.loads(text)
print(dictText['company'])

employee = {
    "name":"Salih",
    "role":"AI Engineer"
}

with open('employee.json','w') as file:
    json.dump(employee,file)

with open('employee.json','r') as file:
    data=json.load(file)
    print(data)