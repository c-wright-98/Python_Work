mark = int(input("Enter the mark: "))

if mark > 85:
    print("Distinction")
if mark >= 65 and mark <= 85:
    print("Pass")
if mark < 65:
    print("Fail")

## Elif statements

mark = int(input("Enter the mark: "))

if mark > 85:
    print("Distinction")
elif mark >= 65:
    print("Pass")
else:
    print("Fail")
