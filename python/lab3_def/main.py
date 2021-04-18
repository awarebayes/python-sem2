# y = sin x
# newton 
# >> a, b (-2, 2)
# find root, no plot

import math as m
import tkinter as tk

f = lambda x: m.sin(x)
f_dx = lambda x: m.cos(x)
eps = 0.001


def newton(a, b):
    x = (a + b) / 2
    print(x, f(x))
    while (abs(f(x)) > eps):
        print(x, f(x))
        x = x - f(x)/f_dx(x)
    return x

def root_callback():
    a = float(a_var.get())
    b = float(b_var.get())
    res = newton(a, b)
    res_var.set(res)

root = tk.Tk()
root.title("Lab 3")

a_var = tk.StringVar()
b_var = tk.StringVar()
res_var = tk.StringVar(value="Result will be shown here")

a_label = tk.Label(text="A:", font="Inconsolata 14")
a = tk.Entry(textvariable=a_var, font="Inconsolata 14")

b_label = tk.Label(text="B:", font="Inconsolata 14")
b = tk.Entry(textvariable=b_var, font="Inconsolata 14")

res = tk.Label(textvariable=res_var, font="Inconsolata 14")

a.grid(row=0, column=1)
a_label.grid(row=0, column=0)

b.grid(row=2, column=1)
b_label.grid(row=2, column=0)

res.grid(row=3, column=0, columnspan=2)

calc_button = tk.Button(text="Calc", command=root_callback, font="Inconsolata 14")
calc_button.grid(row=4)

root.mainloop()
    