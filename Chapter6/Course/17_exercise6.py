employees = {
    "Taylor": {
        "department": "Technology",
        "salary": 3000,
        "grade": 1
    },
    "Luna": {
        "department": "Market",
        "salary": 5000,
        "grade": 2
    },
    "Alex": {
        "department": "Market",
        "salary": 7000,
        "grade": 3
    },
    "Julien": {
        "department": "Technology",
        "salary": 4000,
        "grade": 1
    }
}

names = employees.keys()
for name in names:
    if employees[name]['grade'] == 1:
        employees[name]['salary'] += 1000
        employees[name]['grade'] += 1

print(employees)