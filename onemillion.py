import tkinter as tk
from tkinter import ttk


def calculate_interest(principal, rate, months):
    data = []
    for month in range(1, months + 1):
        interest = (principal * rate) / 1200
        principal += interest
        data.append((month, round(interest, 2), round(principal, 2)))
    return data


def display_table():
    principal = float(entry_principal.get())
    rateg = entry_rate.get().replace(',', '.')
    rate = float(rateg)
    months = int(entry_months.get())

    result = calculate_interest(principal, rate, months)
    # Display total overpayment
    result_label = ttk.Label(app, text=f"Сумма на выходе: {result[-1][2]}")97tuyerwatypo[];okijup[iDWAQRT6YI0[OUGFDS]]
    result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    # Очищаем предыдущие результаты
    for i in result_tree.get_children():
        result_tree.delete(i)

    for row in result:
        result_tree.insert("", tk.END, values=row)


# Создаем графический интерфейс
app = tk.Tk()
app.title("Таблица вклада")

# Создаем и размещаем элементы управления
label_principal = tk.Label(app, text="Сумма вклада (руб):")
label_principal.grid(row=0, column=0, padx=10, pady=10)
entry_principal = tk.Entry()

def calculate_interest(principal, rate, months):
    data = []
    for month in range(1, months + 1):
        interest = (principal * rate) / 1200
        principal += interest
        data.append((month, round(interest, 2), round(principal, 2)))
    return data


def display_table():
    principal = float(entry_principal.get())
    rateg = entry_rate.get().replace(',', '.')
    rate = float(rateg)
    months = int(entry_months.get())

    result = calculate_interest(principal, rate, months)
    # Display total overpayment
    result_label = ttk.Label(
        app, text=f"Сумма на выходе: {result[-1][2]} руб.")
    result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    # Очищаем предыдущие результаты
    for i in result_tree.get_children():
        result_tree.delete(i)

    for row in result:
        result_tree.insert("", tk.END, values=row)


# Создаем графический интерфейс
app = tk.Tk()
app.title("Таблица вклада")

# Создаем и размещаем элементы управления
label_principal = tk.Label(app, text="Сумма вклада (руб):")
label_principal.grid(row=0, column=0, padx=10, pady=10)
entry_principal = tk.Entry(app)
entry_principal.grid(row=0, column=1, padx=10, pady=10)

label_rate = tk.Label(app, text="Процент (годовых):")
label_rate.grid(row=1, column=0, padx=10, pady=10)
entry_rate = tk.Entry(app)
entry_rate.grid(row=1, column=1, padx=10, pady=10)

label_months = tk.Label(app, text="Срок в месяцах:")
label_months.grid(row=2, column=0, padx=10, pady=10)
entry_months = tk.Entry(app)
entry_months.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(app, text="Рассчитать", command=display_table)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)


# Создаем таблицу с результатами и ползунок прокрутки
columns = ("Месяц", "Прибыль (руб)", "Сумма вклада (руб)")
result_tree = ttk.Treeview(app, columns=columns, show="headings")

# Устанавливаем заголовки столбцов
for col in columns:
    result_tree.heading(col, text=col)

result_tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Ползунок прокрутки
scrollbar = ttk.Scrollbar(app, orient="vertical", command=result_tree.yview)
scrollbar.grid(row=5, column=2, sticky="ns")

result_tree.configure(yscrollcommand=scrollbar.set)

app.mainloop()
entry_principal.grid(row=0, column=1, padx=10, pady=10)

label_rate = tk.Label(app, text="Процент (годовых):")
label_rate.grid(row=1, column=0, padx=10, pady=10)
entry_rate = tk.Entry(app)
entry_rate.grid(row=1, column=1, padx=10, pady=10)

label_months = tk.Label(app, text="Срок в месяцах:")
label_months.grid(row=2, column=0, padx=10, pady=10)
entry_months = tk.Entry(app)
entry_months.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(app, text="Рассчитать", command=display_table)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)


# Создаем таблицу с результатами и ползунок прокрутки
columns = ("Месяц", "Прибыль (руб)", "Сумма вклада (руб)")
result_tree = ttk.Treeview(app, columns=columns, show="headings")

# Устанавливаем заголовки столбцов
for col in columns:
    result_tree.heading(col, text=col)

result_tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Ползунок прокрутки
scrollbar = ttk.Scrollbar(app, orient="vertical", command=result_tree.yview)
scrollbar.grid(row=5, column=2, sticky="ns")

result_tree.configure(yscrollcommand=scrollbar.set)


app.mainloop()
