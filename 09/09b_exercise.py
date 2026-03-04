student_records = {
    "student_001":{
        "name":"John", 
        "age":19, 
        "major": "Computer Science", 
        "grades": [85,92,78]
    },
    "student_002":{
        "name": "Sarah", 
        "age": 20, 
        "major":"Biology", 
        "grades": [90,88,95]
    }
}

student_records["student_003"]={
    "name": "Emma",
    "age": 22,
    "major": "kimia",
    "grades": [93,92,99]
}
for student_id, info in student_records.items():
    print(f"{info['name']}({student_id})")
    print(f"    Age: {info['age']}, Major: {info['major']}")
    print(f"    Grades: {info['grades']}")
