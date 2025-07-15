# Version A: Uses f-string output
age = int(input("Enter your age: "))

if age >= 18:
    status = "You are an adult"
else:
    status = "You are a minor"

output = f"Age is {age} so {status}"
print(output)
