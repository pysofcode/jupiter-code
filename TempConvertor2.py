import tkinter as tk
from functools import partial

tempVal = "Целзий"


# външна стойност за конвертирне
def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp


# конвертор
def call_convert(rlabel1, rlabel2, rlabel3, inputn):
    tem = inputn.get()
    if tempVal == 'Целзий':
        f = float((float(tem) * 9 / 5) + 32)
        k = float((float(tem) + 273.15))
        j = float(float(tem)*1899.101)
        rlabel1.config(text="%f Фаренхайт" % f)
        rlabel2.config(text="%f Келвин" % k)
        rlabel3.config(text="%f Джаул" %j)
    if tempVal == 'Фаренхайт':
        c = float((float(tem) - 32) * 5 / 9)
        k = c + 273
        j = float(((float(tem) - 32) * 5 / 9)*1899.101)
        rlabel1.config(text="%f Целзий" % c)
        rlabel2.config(text="%f Келвин" % k)
        rlabel3.config(text="%f Джаул" % j)
    if tempVal == 'Келвин':
        c = float((float(tem) - 273.15))
        f = float((float(tem) - 273.15) * 1.8000 + 32.00)
        j = c*1899.101
        rlabel1.config(text="%f Целзий" % c)
        rlabel2.config(text="%f Фаренхйт" % f)
        rlabel3.config(text="%f Джаул" % j)
    if tempVal == "Джаул":
        c = float(float(tem)/1899.101)
        f = ((c * 9 / 5) + 32)
        k = c + 273
        rlabel1.config(text="%f Целзий" % c)
        rlabel2.config(text="%f Фаренхйт" % f)
        rlabel3.config(text="%f Келвин" % k)

    return


# конфигуриране на прозореца
root = tk.Tk()
root.geometry('500x150+200+200')
root.title('Температурен конвертор')
root.configure(background='#010f12')
root.resizable(width=True, height=True)
root.grid_columnconfigure(1, weight=2)
root.grid_rowconfigure(0, weight=2)

numberInput = tk.StringVar()
var = tk.StringVar()

# поле за въвеждане
input_label = tk.Label(root, text="Въведи температура", background='#010f12', foreground="#FFFFFF")
input_entry = tk.Entry(root, textvariable=numberInput)
input_label.grid(row=1)
input_entry.grid(row=1, column=1)

# показване на другите температурни стойноти
result_label1 = tk.Label(root, background='#010f12', foreground="#FFFFFF")
result_label1.grid(row=3, columnspan=4)
result_label2 = tk.Label(root, background='#010f12', foreground="#FFFFFF")
result_label2.grid(row=4, columnspan=4)
result_label3 = tk.Label(root, background='#010f12', foreground="#FFFFFF")
result_label3.grid(row=5, columnspan=4)


# падащо меню
dropDownList = ["Целзий", "Фаренхайт", "Келвин", "Джаул"]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=store_temp)
var.set(dropDownList[0])
dropdown.grid(row=1, column=2)
dropdown.config(background='#45777e', foreground="#FFFFFF")
dropdown["menu"].config(background='#45777e', foreground="#FFFFFF")

# функиция на бутона
call_convert = partial(call_convert, result_label1, result_label2, result_label3, numberInput)
result_button = tk.Button(root, text="Конвертирай", command=call_convert, background='#45777e', foreground="#FFFFFF")
result_button.grid(row=2, columnspan=5)

root.mainloop()
