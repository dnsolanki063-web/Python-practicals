#assignment pre_6

employee = {
    "name": "Krishna",
    "qualification": "MCA",
    "Experience": '4 years',
    "age": 30
}
print("Dictionary:", employee)
print("Student Name:", employee["name"])
print("Qualification:", employee["qualification"])
print("Experience of employee:", employee.get("experience"))
print("Age :",employee.get("age"))

employee["age"] = 28
employee["Experience"] = "3 years"
print("Dictionary after changing values:",employee)
print("Number of items:", len(employee))