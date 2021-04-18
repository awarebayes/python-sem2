import tkinter as tk
import numpy as np

N_MAX = 10_000
PADDING = 2

# ROOTS

untils = {
    "f": lambda g, f, x, eps: abs(f(x)) > eps,
    "g": lambda g, f, x, eps: abs(g(x) - x) > eps,
}


def iter_root(g, f, x, eps, until):
    n = 0
    ec = 0
    while until(g, f, x, eps):
        try:
            x = g(x)
        except ZeroDivisionError:
            ec = 2
        n += 1
        if n > N_MAX:
            ec = 1
            break
    return x, n, ec


g_x = lambda x: 1 / ((1 + x) ** 0.5)
f_x = lambda x: x ** 3 + x ** 2 - 1


def find_root_intervals(f, a, b, h):
    ls = np.arange(a, b + h, h)
    for i, i_next in zip(ls, ls[1:]):
        if f(i) * f(i_next) < 0:
            yield i, i_next


def root_info(a, b, s, eps, until):
    root_n = 1
    for st, en in find_root_intervals(f_x, a, b, s):
        middle = (st + en) / 2
        root, n_iter, ec = iter_root(g_x, f_x, middle, eps, until)

        yield [root_n, f"({st:.6f}, {en:.6f})", root, f_x(root), n_iter, ec]

        root_n += 1

def extremums(arr):
    for i in range(1, len(arr)-1):
        if arr[i-1] > arr[i] < arr[i+1] or \
           arr[i-1] < arr[i] > arr[i+1]:
            yield i

### TKINTER

# UI


def process_text(a):
    if isinstance(a, float):
        a = f"{a:.6f}"
    elif not isinstance(a, str):
        a = str(a)
    return f"{' '*PADDING}{a}{' ' * PADDING}"


def yield_cells(rows):
    for row in rows:
        for col in row:
            if isinstance(col, tk.StringVar):
                cell = tk.Label(textvariable=col, font="Inconsolata 12")
            else:
                text = process_text(col)
                cell = tk.Label(text=text, font="Inconsolata 12")
            yield cell


def gen_table(rows, grid_start_row, grid_start_col):
    n_cols = len(rows[0])
    idx = 0
    for cell in yield_cells(rows):
        col = grid_start_col + idx % n_cols
        row = grid_start_row + idx // n_cols
        idx += 1
        cell.grid(column=col, row=row)


def multiple_input_form(labels, vars, row_start, col_start):
    n = 0
    for label, var in zip(labels, vars):
        l = tk.Label(text=label, font="Inconsolata 14")
        e = tk.Entry(textvariable=var, font="Inconsolata 14")
        l.grid(column=col_start, row=row_start + n)
        e.grid(column=col_start + 1, row=row_start + n)
        n += 1

def get_vars():
    return map(float, map(tk.StringVar.get, [a_var, b_var, s_var, eps_var]))

def regen_table():
    a, b, s, eps = get_vars()

    info = root_info(a, b, s, eps, untils[until_var.get()])
    table = [["Root n", "[x_i, x_{i+1}]", "x", "f(x)", "N ITER", "Error"], *info]
    gen_table(table, 8, 0)

def show_plot():
    import matplotlib.pyplot as plt
    a, b, s, _ = get_vars()
    x = np.arange(a, b, s)
    y = f_x(x)
    plt.plot(x, y)
    ext_idx = list(extremums(y))
    ext_x: np.ndarray = np.take(x, ext_idx)
    ext_y = f_x(ext_x)
    plt.scatter(ext_x, ext_y)
    plt.grid()
    plt.show()


# Init
root = tk.Tk()
root.title("Roots")

a_var = tk.StringVar()
b_var = tk.StringVar()
s_var = tk.StringVar()
eps_var = tk.StringVar()
until_var = tk.StringVar(value='f')

multiple_input_form(
    ["Start", "End", "Step", "Epsilon"], [a_var, b_var, s_var, eps_var], 0, 0
)

until_f = tk.Radiobutton(text="abs(f) > eps", value="f", variable=until_var, font="Inconsolata 14")
until_g = tk.Radiobutton(text="abs(g(x)-x) > eps", value="g", variable=until_var, font="Inconsolata 14")
until_f.grid(row=5, column=0)
until_g.grid(row=5, column=1)


generate_btn = tk.Button(text="Generate", font="Inconsolata 14", command=regen_table)
generate_btn.grid(column=0, row=6, columnspan=2)

plot_btn = tk.Button(text="Plot", font="Inconsolata 14", command=show_plot)
plot_btn.grid(column=0, row=7, columnspan=2)

root.mainloop()
