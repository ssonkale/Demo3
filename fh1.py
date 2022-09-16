import json

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('file.json', 'w') as fh:
  json.dump(person_dict, fh)

with open('file.json', 'r') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)