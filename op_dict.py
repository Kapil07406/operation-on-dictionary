# Operations on Dictionary

student = {
    "Name": "Kapil",
    "Age": 20,
    "City": "Delhi"
}

print("Original Dictionary")
print(student)

# Add
student["Marks"] = 95

# Update
student["Age"] = 21

# Delete
del student["City"]

print("\nUpdated Dictionary")
print(student)

print("\nKeys")
print(student.keys())

print("\nValues")
print(student.values())

print("\nItems")
print(student.items())