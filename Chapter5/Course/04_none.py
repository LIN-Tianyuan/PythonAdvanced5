def check_age(age):
    if age > 18:
        return "SUCCESS"
    return None

result = check_age(5)
if not result:
    print("No enter!")