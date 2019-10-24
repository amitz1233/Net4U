import json


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y=json.dumps(x)
Res11=open("C:/Users/Pc/Desktop/json.txt", "r")
l=Res11.read()
print(l)