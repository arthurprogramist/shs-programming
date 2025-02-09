number = 15
print(number)
print(type(number))

float_num = 14.545679
print(float_num)
print(type(float_num))

string = "Привет, python!"
print(string)
print(type(string))

bool_ = True  # False
print(bool_)
print(type(bool_))

print(number + float_num)
print(number - float_num)
print(number * float_num)
print(number / float_num)
print(number // float_num)
print(number % float_num)
print(number ^ 2)

print(int(float_num))
print(round(float_num, 2))

print(string + " Ты очень интересный!")
print(string, "Ты очень интересный!")

num1, num2 = 10, 11

if num1 < num2:
    print("Меньше")
elif num1 > num2:
    print("Больше")
elif num1 >= num2:
    print("Больше и равно")
elif num1 <= num2:
    print("Меньше и равно")
else:
    pass
