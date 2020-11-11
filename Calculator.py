from tkinter import *


def on_hover(event):
    event.widget.configure(bg="#000000", fg="#ffffff")


def off_hover(event):
    event.widget.configure(bg="#ffffff", fg="#000000")


def on_operator_hover(event):
    event.widget.configure(bg="#EC6124", fg="#ffffff")


def off_operator_hover(event):
    event.widget.configure(bg="#ffffff", fg="#000000")


def on_clear_hover(event):
    event.widget.configure(bg="#FF0000", fg="#000000")


def off_clear_hover(event):
    event.widget.configure(bg="#ffffff", fg="#000000")


def on_Kyes_clicked(event):
    user_input = event.widget.cget("text")
    if user_input == "=":
        value = eval(input_area.get())
        data.set(int(value))
        input_area.update()
    elif user_input == "Clear":
        input_area.delete(0, END)
    else:
        data.set(data.get() + user_input)
        input_area.update()


root = Tk()
root.title("My Calculator")
root.iconbitmap(r'./img/Calculator_logo.ico')
root.geometry("252x300+600+200")
root.resizable(0, 0)
root.configure(bg="#ffffff")

data = StringVar()
data.set("")

input_area = Entry(root, text=data, font=('arial', 14, 'bold'), width=21, justify='right', bd=10, bg="#ffffff")
input_area.pack(padx=5, pady=5)

btnFrame = Frame(root, bg="#ffffff")
btnFrame.pack(side=TOP)

btn1 = Button(btnFrame, text="1", font=("Verdana", 10, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=18, pady=10)
btn2 = Button(btnFrame, text="2", font=("Verdana", 10, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=18, pady=10)
btn3 = Button(btnFrame, text="3", font=("Verdana", 10, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=18, pady=10)
btn4 = Button(btnFrame, text="4", font=("Verdana", 10, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=18, pady=10)
btn5 = Button(btnFrame, text="5", font=("Verdana", 10, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=18, pady=10)
btn6 = Button(btnFrame, text="6", font=("Verdana", 10, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=18, pady=10)
btn7 = Button(btnFrame, text="7", font=("Verdana", 10, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=18, pady=10)
btn8 = Button(btnFrame, text="8", font=("Verdana", 10, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=18, pady=10)
btn9 = Button(btnFrame, text="9", font=("Verdana", 10, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=18, pady=10)
btn0 = Button(btnFrame, text="0", font=("Verdana", 10, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=18, pady=10)

add = Button(btnFrame, text="+", font=("Verdana", 14, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=12, pady=4)
Sub = Button(btnFrame, text="-", font=("Verdana", 14, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=15, pady=4)
Mul = Button(btnFrame, text="*", font=("Verdana", 14, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=13, pady=4)
Div = Button(btnFrame, text="/", font=("Verdana", 14, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=13, pady=4)

Equal = Button(btnFrame, text="=", font=("Verdana", 14, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=12, pady=4)
point = Button(btnFrame, text=".", font=("Verdana", 14, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=16, pady=4)
Clear = Button(root, text="Clear", font=("Verdana", 14, "bold"), bd=5, bg="#ffffff", fg="#000000", padx=16, pady=4)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

add.grid(row=1, column=3)
Sub.grid(row=2, column=3)
Mul.grid(row=3, column=3)
Div.grid(row=4, column=3)

btn0.grid(row=4, column=1)
Equal.grid(row=4, column=2)
point.grid(row=4, column=0)
Clear.pack(fill=X)

btn1.bind("<Button-1>", on_Kyes_clicked)
btn2.bind("<Button-1>", on_Kyes_clicked)
btn3.bind("<Button-1>", on_Kyes_clicked)
btn4.bind("<Button-1>", on_Kyes_clicked)
btn5.bind("<Button-1>", on_Kyes_clicked)
btn6.bind("<Button-1>", on_Kyes_clicked)
btn7.bind("<Button-1>", on_Kyes_clicked)
btn8.bind("<Button-1>", on_Kyes_clicked)
btn9.bind("<Button-1>", on_Kyes_clicked)
btn0.bind("<Button-1>", on_Kyes_clicked)
Equal.bind("<Button-1>", on_Kyes_clicked)
add.bind("<Button-1>", on_Kyes_clicked)
Sub.bind("<Button-1>", on_Kyes_clicked)
Mul.bind("<Button-1>", on_Kyes_clicked)
Div.bind("<Button-1>", on_Kyes_clicked)
point.bind("<Button-1>", on_Kyes_clicked)
Clear.bind("<Button-1>", on_Kyes_clicked)

btn1.bind("<Enter>", on_hover)
btn2.bind("<Enter>", on_hover)
btn3.bind("<Enter>", on_hover)
btn4.bind("<Enter>", on_hover)
btn5.bind("<Enter>", on_hover)
btn6.bind("<Enter>", on_hover)
btn7.bind("<Enter>", on_hover)
btn8.bind("<Enter>", on_hover)
btn9.bind("<Enter>", on_hover)
btn0.bind("<Enter>", on_hover)
point.bind("<Enter>", on_hover)
add.bind("<Enter>", on_operator_hover)
Sub.bind("<Enter>", on_operator_hover)
Mul.bind("<Enter>", on_operator_hover)
Div.bind("<Enter>", on_operator_hover)
Equal.bind("<Enter>", on_operator_hover)
Clear.bind("<Enter>", on_clear_hover)

btn1.bind("<Leave>", off_hover)
btn2.bind("<Leave>", off_hover)
btn3.bind("<Leave>", off_hover)
btn4.bind("<Leave>", off_hover)
btn5.bind("<Leave>", off_hover)
btn6.bind("<Leave>", off_hover)
btn7.bind("<Leave>", off_hover)
btn8.bind("<Leave>", off_hover)
btn9.bind("<Leave>", off_hover)
btn0.bind("<Leave>", off_hover)
point.bind("<Leave>", off_hover)
add.bind("<Leave>", off_operator_hover)
Sub.bind("<Leave>", off_operator_hover)
Mul.bind("<Leave>", off_operator_hover)
Div.bind("<Leave>", off_operator_hover)
Equal.bind("<Leave>", off_operator_hover)
Clear.bind("<Leave>", off_clear_hover)

root.mainloop()
