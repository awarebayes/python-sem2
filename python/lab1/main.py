# Написал Щербина МА ИУ7-25Б

import tkinter as tk
from tkinter import messagebox
from math import ceil, log
from expr_tree import eval_string

root = tk.Tk()
root.title("Calculator")

BUTTON_WIDTH = 3
BUTTON_HEIGHT = 3

# Vars
result = tk.StringVar()
is_bin = tk.BooleanVar()


# Initialize number buttons
def init_buttons(labels):
    for label in labels:
        # https://github.com/satwikkansal/wtfpython#-schr%C3%B6dingers-variable-
        def callback(label=label):
            index = len(result.get())
            result_entry.insert(index, label)

        yield tk.Button(
            root, text=label, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=callback
        )


# about info
def about():
    messagebox.showinfo(
        title="About", message="Автор: Михаил Щербина ИУ7-25Б\nGPL3 License"
    )


# Clear result, called by AC
def clear():
    result.set("")


# Calculate string in result, get result
def calculate():
    res = eval_string(result.get())
    if res is None:
        messagebox.showerror(
            title="Error", message="Something is wrong with your expression!"
        )
    else:
        result.set(str(res))


# append new symbol to result
def append_sym(symbol, target):
    target.set(target.get() + symbol)


def bin_add_one(bin_str):
    carry_over = True
    res = []
    for i in reversed(bin_str):
        if carry_over:
            if i == "1":
                res.append("0")
            if i == "0":
                res.append("1")
                carry_over = False
        else:
            res.append(i)
    return "".join(reversed(res))


invert_bin = {"1": "0", "0": "1"}.get

# my bin function
def my_bin(dec_str):
    num = int(dec_str)
    n_bits = ceil((ceil(log(abs(num), 2)) + 1) / 8) * 8
    res = ["0" for _ in range(n_bits)]
    if num > 0:
        for i in range(n_bits):
            if num % 2 != 0:
                res[i] = "1"
            num //= 2
    else:
        # get rid of sign
        inversed = my_bin(str(-num))
        # invert
        inverted = "".join(map(invert_bin, inversed))
        # add one
        one_added = bin_add_one(inverted)
        return one_added  # strip

    return "".join(reversed(res))


# my int function
def my_int(bin_str, ignore_first=False):
    if bin_str[0] == "1" and not ignore_first:
        inversed = "".join(map(invert_bin, bin_str[1:]))
        return "-" + my_int(bin_add_one(inversed), True)
    res = 0
    cur_pow = 1
    for i in reversed(bin_str):
        if i == "1":
            res += cur_pow
        cur_pow *= 2
    return str(res)


# toggle bin
def to_bin():
    # initial result from entry
    init_res = result.get().strip()
    if not init_res:
        # toggle back
        is_bin.set(not (is_bin.get()))
        return
    try:
        if is_bin.get():  # int -> bin
            res = my_bin(result.get())
            result.set(res)
        else:  # bin -> int
            res = my_int(init_res)
            result.set(res)
    except:
        messagebox.showerror(
            title="Error", message="Something is wrong with your expression!"
        )


# make manu from labels
def make_menu(master, labels):
    for label in labels:
        # https://github.com/satwikkansal/wtfpython#-schr%C3%B6dingers-variable-
        def callback(label=label):
            index = len(result.get())
            result_entry.insert(index, label)

        master.add_command(label=label, command=callback, font="12")


# Menus

mainmenu = tk.Menu(root)
root.config(menu=mainmenu)

options = ["+", "-", "/", "*", ".", "//", "%", "^", "√", "(", ")"]
options_menu = tk.Menu(mainmenu, tearoff=0)
make_menu(options_menu, options)
options_menu.add_checkbutton(label="To bin", command=to_bin, variable=is_bin)
mainmenu.add_cascade(label="Options", menu=options_menu)

mainmenu.add_command(label="Clear", command=clear)
mainmenu.add_command(label="About", command=about)

# Result Entry
result_entry = tk.Entry(root, width=16, textvariable=result, font="Inconsolata 12")
result_entry.grid(column=0, row=0, columnspan=5)

# Buttons

# Numbers
button_labels = list(map(str, range(1, 10))) + ["0", "."]
buttons = init_buttons(button_labels)
for i, b in enumerate(buttons):
    b.grid(column=0 + i % 3, row=1 + i // 3)

# Operators
button_labels = ["+", "-", "/", "*"]
buttons = init_buttons(button_labels)
for i, b in enumerate(buttons):
    b.grid(column=4, row=i + 1)

# =
calculate_btn = tk.Button(root, text="=", width=22, command=calculate)
calculate_btn.grid(column=0, row=5, columnspan=5)

# AC
clear_btn = tk.Button(
    root, text="AC", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=clear
)
clear_btn.grid(column=2, row=4)

# To binary
to_bin_btn = tk.Checkbutton(
    root, text="To binary", width=20, variable=is_bin, command=to_bin
)
to_bin_btn.grid(column=0, row=6, columnspan=5)

root.mainloop()
