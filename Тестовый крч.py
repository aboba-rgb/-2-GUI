import tkinter as tk


def append_to_expression(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_expression + str(value))


def clear_expression():
    entry.delete(0, tk.END)


def calculate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")

# Создаем поле для ввода
entry = tk.Entry(root, width=16, font=('Arial', 24), justify='right')
entry.pack(padx=10, pady=10)

# Создаем кнопки
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Создаем кнопку с функцией
for button in buttons:
    if button == 'C':
        b = tk.Button(root, text=button, command=clear_expression, width=5, height=2)
    elif button == '=':
        b = tk.Button(root, text=button, command=calculate_expression, width=5, height=2)
    else:
        b = tk.Button(root, text=button, command=lambda value=button: append_to_expression(value), width=5, height=2)

    b.pack(side=tk.LEFT, padx=5, pady=5)

# Запускаем главный цикл
root.mainloop()