import tkinter as tk

months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

def change_month(step):
    global c_month
    c_month = (c_month + step) % 12
    draw_calendar()

def draw_calendar():
    month_label.config(text=months[c_month])
    for widget in days_frame.winfo_children():
        widget.destroy()

    weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

    for column, name in enumerate(weekdays):
        w_days = tk.Label(days_frame, text=name, font=("Arial", 12, "bold"), relief="solid", bd=1, padx=8, pady=10)
        w_days.grid( row=1, column=column, sticky="nsew", padx=1, pady=1)

    for day in range(1, 31):
        row = (day - 1) // 7
        column = (day - 1) % 7
        tk.Label(days_frame, text=day, font=("Arial", 12, "bold"), relief="solid", bd=1, padx=25, pady=10).grid(row=row + 2, column=column)


calendar = tk.Tk()
calendar.title("Календарь")
calendar.geometry("500x500")
calendar.minsize(300, 300)
c_month=0

month_label = tk.Label(calendar, text=months[c_month], font=("Arial", 24, "bold"), relief="solid", bd=1, padx=8, pady=10)
month_label.grid(row=0, column=0, columnspan=10)

days_frame = tk.Frame(calendar)
days_frame.grid(row=2, column=0, columnspan=5, sticky='nsew')

prev_button = tk.Button(calendar, text="<", command=lambda: change_month(-1), font=("Arial", 18), width=3,height=2)
next_button = tk.Button(calendar, text=">", command=lambda: change_month(1), font=("Arial", 18), width=3,height=2)
prev_button.grid(row=0, column=0, columnspan=1, padx=(12, 5), pady=10, sticky="nw")
next_button.grid(row=0, column=3, columnspan=1, padx=(12, 5), pady=10, sticky="ne")


calendar.grid_columnconfigure(1, weight=1)
calendar.grid_rowconfigure(2, weight=1)

for column in range(7):
    days_frame.grid_columnconfigure(column, weight=1, uniform="days")

for row in range(8):
    days_frame.grid_rowconfigure(row, weight=1, uniform="days")


draw_calendar()

calendar.mainloop()