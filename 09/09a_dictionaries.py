student = {
    "name": "Alice",
    "Age" : 20,
    "Grade": "A",
    "Courses": ["Math", "Science", "English"]
}
'''
#Accessing and modify
print(student["name"])     #checking
print(student.get("Age"))  #same, prefer to use no 1
student["Age"] = 21        #modiffy
student["email"]= "azimazmi" #add
print(student["Age"])
print(student)

# keys and values are separated by :
keys = student.keys()
values = student.values()
items = student.items()

print(keys)
print(values)
print(items)

#iteration
for key in student: 
    print(f"{key}:{student[key]}")

for key, value in student.items():
    print(f"{key}:{value}")
'''
#nested
company = {
    "employees": {
        "john" : {"age": 30, "department": "it"},
        "jane": {"Age": 25, "department": "hr"}
    },
    "department": ["it", "hr", "finance"] 
}

print(company["employees"].items())
print(company["department"])