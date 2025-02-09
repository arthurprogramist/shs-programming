passw = input("Введите пароль: ")

def checkpassword(password):
    if len(password) < 8:
        return False
    if not any(i.isdigit() for i in password):
        return False
    if not any(i.islower() for i in password):
        return False
    if not any(i.isupper() for i in password):
        return False
    return True
if checkpassword(passw):
    print("надеждный пароль")
else:
    print("Пароль не подходит, придумайте другой, который Содержит минимум 8 символов; Включает хотя бы одну цифру; Содержит заглавную и строчную букву")
