chislo = input("Введите четырехзначное число: ")


a = 1
for o in chislo:
    a *= int(o)

print("Произведение: ", a)