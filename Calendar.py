import tkinter as tk
from tkinter import messagebox
from datetime import datetime



months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

def change_month(step):  # функция для листания месяцев
    global c_month
    c_month = (c_month + step) % 12
    draw_calendar()

def draw_calendar():   # основная функция для отображения календаря (будет повторяться с каждым пролистыванием)
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
   
# ==== доп функции ====
        
def add_event(): # запланировать событие на день
    pass

def date_calculator():  #  считать дни (в отдельном окне)
    date_cal = tk.Toplevel(extra_frame)
    date_cal.title('Калькулятор дат')
    date_cal.geometry('500x500')
    
    def calculate_days():
        try:
            date_str1 = entry1.get().strip()
            date_str2 = entry2.get().strip()

            date1 = datetime.strptime(date_str1, "%d.%m.%Y")
            date2 = datetime.strptime(date_str2, "%d.%m.%Y")

            delta = abs(date2 - date1)

            label_result.config(text=f"Разница: {delta.days} дней", fg="green")
        except ValueError:
            messagebox.showerror("Ошибка формата", "Введите даты в формате ДД.ММ.ГГГГ\n(Например: 26.10.2026)",)
            
    
    label1 = tk.Label(date_cal, text="начальная дата: ", font=("Arial", 14, "bold"))
    label1.pack(pady=10)
    entry1 = tk.Entry(date_cal, justify='center', font=("Arial", 14, "bold"))
    entry1.pack(pady=5)
    entry1.insert(0,datetime.now().strftime("%d.%m.%Y"))
    
    label2 = tk.Label(date_cal,text='конечная дата: ', font=("Arial", 14, "bold"))
    label2.pack(pady=15)
    entry2 = tk.Entry(date_cal, justify='center', font=("Arial", 14, "bold"))
    entry2.pack(pady=10)
    entry2.insert(0,datetime.now().strftime("%d.%m.%Y"))

    btn_calc = tk.Button(date_cal, text="Посчитать дни", command=calculate_days,bg="#9689de", font=("Arial", 14, "bold"))
    btn_calc.pack(pady=20)
    
    label_result = tk.Label(date_cal,text='Разница: ',font=("Arial",12,'bold'))
    label_result.pack(padx=50,pady=30)
    
# ==== конфигурация корня ====

calendar = tk.Tk()
calendar.title("Календарь")
calendar.geometry("500x500")
calendar.minsize(300, 300)
c_month=0

month_label = tk.Label(calendar, text=months[c_month], font=("Arial", 24, "bold"), relief="solid", bd=1, padx=8, pady=10)
month_label.grid(row=0, column=0, columnspan=10)

# ==== фреймы ====

days_frame = tk.Frame(calendar)  #  часть где распологаютсья дни
days_frame.grid(row=2, column=0, columnspan=5, sticky='nsew')

func_frame=tk.Frame(calendar)  #  часть где распологаеться кнопочки месяцев
func_frame.grid()

extra_frame = tk.Frame(calendar) #  часть где распологаеться доп. функционал
extra_frame.grid()

# ==== бинды ====

prev_button = tk.Button(calendar, text="<", command=lambda: change_month(-1), font=("Arial", 18), width=3,height=2)
next_button = tk.Button(calendar, text=">", command=lambda: change_month(1), font=("Arial", 18), width=3,height=2)
prev_button.grid(row=0, column=0, columnspan=1, padx=(12, 5), pady=10, sticky="nw")
next_button.grid(row=0, column=3, columnspan=1, padx=(12, 5), pady=10, sticky="ne")

baton_cal = tk.Button(extra_frame, text='калькулятор дат', command=date_calculator,bg="#d6f4c8")
baton_cal.pack(pady=10, padx=5)


calendar.grid_columnconfigure(1, weight=1)
calendar.grid_rowconfigure(2, weight=1)

for column in range(7):
    days_frame.grid_columnconfigure(column, weight=1, uniform="days")

for row in range(8):
    days_frame.grid_rowconfigure(row, weight=1, uniform="days")
    
    

draw_calendar()

calendar.mainloop()
