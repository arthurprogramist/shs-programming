import tkinter as tk
import random as rand


def vivod(user):
    options = ["камень", "бумага", "ножницы"]
    computer = rand.choice(options)  # компьютер случайно выбирает что то из списка options
    result_label.config(text=f"Ты выбрал: {user}\nКомпьютер выбрал: {computer}")  # вывод нашего выбора и выбора компа

    if user == computer:  # условие как раньше, только немного упрощенное
        outcome = "Ничья!"
    elif (user == "камень" and computer == "ножницы") or \
         (user == "бумага" and computer == "камень") or \
         (user == "ножницы" and computer == "бумага"):
        outcome = "Ты выиграл!"
    else:
        outcome = "Ты проиграл!"

    outcome_label.config(text=outcome)

# Создаем и даем имя окну
root = tk.Tk()
root.title("КНБ!")

# Вывод сообщения "Выберите один из вариантов:"
label = tk.Label(root, text="Выберите один из вариантов:", font=14)
label.pack(pady=10)

# Тут все кнопки для игры
button_rock = tk.Button(root, text="Камень", width=20, height=2, command=lambda: vivod("камень"))
button_rock.pack(pady=5)

button_paper = tk.Button(root, text="Бумага", width=20, height=2, command=lambda: vivod("бумага"))
button_paper.pack(pady=5)

button_scissors = tk.Button(root, text="Ножницы", width=20, height=2, command=lambda: vivod("ножницы"))
button_scissors.pack(pady=5)

result_label = tk.Label(root, text="", font=12)
result_label.pack(pady=10)

outcome_label = tk.Label(root, text="", font=12)
outcome_label.pack(pady=10)

# обязательная комманда для запуска нашего окна
root.mainloop()
