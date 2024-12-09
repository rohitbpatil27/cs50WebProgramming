people = [
    {"name":"Rohit","surname":"Patil"},
    {"name":"Estaa","surname":"Patil"},
    {"name":"Namrata","surname":"Mahindrakar"}
]

people.sort(key=lambda person:person["name"])

print(people)