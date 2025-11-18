student = {"Kyla": 85,"Khen": 90,"Greg": 78,"Rhanz": 88,"Kyle": 92,"Limuel": 75,"Raven": 80,"Josh": 89,"Ismael": 95,"Mhel": 70,"Maui": 84,"Hazel": 91,"Carlo": 76,"Kim": 87,"Carl": 82,"Jomari": 93,"Luke": 88}

print("Student list")
print(student)

print("\nSpecific students grade")
print("Khen's grade is ", student["Khen"])

print("\nADD STUDENT")
student["Lei"] = 89
print(student)

print("\nUpdate one student")
student["Khen"] = 95
print(student)

print("\nDelete one student")
del student["Greg"]
print(student)
