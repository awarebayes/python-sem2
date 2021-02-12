from tkinter import *
from tkinter import messagebox
from expr_tree import eval_string
from math import ceil, log

root = Tk()
root.title("Calculator")

BUTTON_WIDTH = 2
BUTTON_HEIGHT = 2


def init_buttons(button_labels):
    for label in button_labels:
        # https://github.com/satwikkansal/wtfpython#-schr%C3%B6dingers-variable-
        def callback(label=label):
            index = len(result.get())
            result_entry.insert(index, label)

        yield Button(
            root, text=label, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=callback
        )


def about():
    messagebox.showinfo(
        title="About", message="Автор: Михаил Щербина ИУ7-25Б\nBSD2 License")


def clear():
    result.set("")


def calculate():
    res = eval_string(result.get())
    if res is None:
        messagebox.showerror(
            title="Error", message="Something is wrong with your expression!"
        )
    else:
        result.set(str(res))


def append_sym(symbol, target):
    target.set(target.get() + symbol)


def my_bin(decimal_str):
    decimal = int(decimal_str)
    n_digits = ceil(log(int(decimal), 2))
    numbers = ['' for i in range(n_digits)]
    c_num = 0
    while decimal > 0:
        numbers[c_num] = str(decimal % 2)
        decimal //= 2
        c_num += 1
    return ''.join(reversed(numbers))


def my_int(bin_str):
    res = 0
    cur_pow = 1
    for i in reversed(bin_str):
        if i == '1':
            res += cur_pow
        cur_pow *= 2
    return str(res)


def to_bin():
    try:
        if is_bin.get():
            res = int(result.get())
            if res < 0:
                raise ValueError
            res = my_bin(result.get())
            result.set(res)
        else:
            res = my_int(result.get())
            result.set(res)
        # is_bin.set(not(is_bin.get()))
    except:
        messagebox.showerror(
            title="Error", message="Something is wrong with your expression!"
        )


def make_menu(master, labels):
    for label in labels:
        # https://github.com/satwikkansal/wtfpython#-schr%C3%B6dingers-variable-
        def callback(label=label):
            index = len(result.get())
            result_entry.insert(index, label)
        master.add_command(label=label, command=callback)

# Menus


mainmenu = Menu(root)
root.config(menu=mainmenu)


options = ["+", "-", "/", "*", ".", "//", "%", "^", "√", "(", ")"]
options_menu = Menu(mainmenu, tearoff=0)
make_menu(options_menu, options)
mainmenu.add_cascade(label="Options", menu=options_menu)

mainmenu.add_command(label="Clear", command=clear)
mainmenu.add_command(label="About", command=about)

# Result Entry
result = StringVar()
result_entry = Entry(root, width=16, textvariable=result, font="16")
result_entry.grid(column=0, row=0, columnspan=5)


# Buttons

button_labels = list(map(str, range(1, 10))) + ["0", "."]
buttons = init_buttons(button_labels)
for i, b in enumerate(buttons):
    b.grid(column=0 + i % 3, row=1 + i // 3)

button_labels = ["+", "-", "/", "*"]
buttons = init_buttons(button_labels)

for i, b in enumerate(buttons):
    b.grid(column=4, row=i + 1)

calculate_btn = Button(root, text="=", width=18, command=calculate)
calculate_btn.grid(column=0, row=5, columnspan=5)

clear_btn = Button(
    root, text="AC", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=clear
)
clear_btn.grid(column=2, row=4)

is_bin = BooleanVar()
to_bin_btn = Checkbutton(root, text="To binary", width=20,
                         variable=is_bin, command=to_bin)
to_bin_btn.grid(column=0, row=6, columnspan=5)

root.mainloop()
