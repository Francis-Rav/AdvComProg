grade = int(input("Enter Grade "))
if grade <= 0 or grade >= 101:
    print("Invalid")
else:
    print("Valid")
    if grade >= 90:
        print("pass")
    elif grade >=76:
        print("pass")
    else:
        print("go back")
