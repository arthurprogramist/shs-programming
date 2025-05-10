# age = 0
# status = 'adult/child'
#
#


name = input("Enter your name: ")
print(f"Your name is {name}")

age = int(input("Enter your age: "))
print(f"Your age is {age}")

if age < 18:
    print("ur teen")
    status = "teen"

else:
    print("ur teen")
    status = "adult"
fuf = f"""=========

========="""
if status == "teen":
     print("ИДИ УЧИ УРОКИ")
else:
     print("ИДИ РАБОТАЙ")

form = f"""=====================
Hi {name}! \nYou {age} years old.
You are {status} \n 
====================="""
print(form)
