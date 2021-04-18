import tkinter as tk
import random
from functools import partial
import timeit


# Sorting algorithm
def barrier_sort(arr):
    arr = [0] + arr
    for i in range(1, len(arr)):
        arr[0] = arr[i]
        j = i - 1
        while arr[0] < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[0]
    return arr[1:]


# Utility

time = partial(timeit.timeit, number=1)


def cmap(x):
    return lambda a: map(x, a)


def compose(*functions):
    def inner(arg):
        for f in reversed(functions):
            arg = f(arg)
        return arg

    return inner


# UI


def yield_cells(rows, padding=2):
    for row in rows:
        for col in row:
            if isinstance(col, tk.StringVar):
                cell = tk.Label(textvariable=col, font="Inconsolata 12")
            else:
                cell = tk.Label(text=col, font="Inconsolata 12")
            yield cell


def gen_table(rows, grid_start_row, grid_start_col):
    n_rows = len(rows)
    n_cols = len(rows[0])
    idx = 0
    for cell in yield_cells(rows):
        col = grid_start_col + idx % n_cols
        row = grid_start_row + idx // n_rows
        idx += 1
        cell.grid(column=col, row=row)


# Generators:
def random_arr(size):
    return [random.randint(0, size) for i in range(size)]


def sorted_arr(size):
    res = [0]
    for i in range(size):
        res.append(random.randint(res[-1], size))
    return res


def reversed_sorted_arr(size):
    return list(reversed(sorted_arr(size)))


# Util functions x2:
def sort_time(arr):
    return time(lambda: barrier_sort(arr))


def serialize_int_list(arr):
    max_len_str = str(len(str(max(arr))))
    len_fmt = "{:" + max_len_str + "}"
    pipe = compose(" ".join, cmap(len_fmt.format))
    return pipe(arr)


# gen func is a generator for array to sort
def time_test(gen_func, callbacks):
    n1, n2, n3 = map(compose(int, lambda x: x.get()), [N1, N2, N3])
    arrays = map(gen_func, [n1, n2, n3])
    for a, cb in zip(arrays, callbacks):
        times = sort_time(a)
        times_fmt = "{:.3e}".format(times)
        cb.set(times_fmt)


def sort_callback():
    arr_small = unsorted_var.get()
    arr_small = list(map(int, arr_small.split()))
    sorted = serialize_int_list(barrier_sort(arr_small))
    sorted_var.set(sorted)


def generate_callback():
    for f, cb in zip([random_arr, sorted_arr, reversed_sorted_arr], callback):
        time_test(f, cb)


arr_small = random_arr(10)

# Init
root = tk.Tk()
root.title("Calculator")


N1 = tk.StringVar()
N2 = tk.StringVar()
N3 = tk.StringVar()

random_res = [tk.StringVar() for i in range(3)]
sorted_res = [tk.StringVar() for i in range(3)]
reversed_res = [tk.StringVar() for i in range(3)]
callback = [random_res, sorted_res, reversed_res]

ns = [N1, N2, N3]
for i in range(3):
    l = tk.Label(text=f"N{i}: ", font="Inconsolata 14")
    l.grid(row=i, column=0)
    e = tk.Entry(textvariable=ns[i], font="Inconsolata 14")
    e.grid(row=i, column=1, columnspan=2)

generate = tk.Button(
    command=generate_callback, text="Generate Table", font="Inconsolata 14"
)
generate.grid(row=3, column=0)


unsorted_var = tk.StringVar()
unsorted_input = tk.Entry(textvariable=unsorted_var, font="Inconsolata 14")
unsorted_input.grid(column=1, row=4, columnspan=2)

unsorted_text = "Unsorted:  "
unsorted_label = tk.Label(text=unsorted_text, font="Inconsolata 14")
unsorted_label.grid(column=0, row=4)


sorted_text = "Sorted:    "
sorted_label = tk.Label(text=sorted_text, font="Inconsolata 14")
sorted_label.grid(column=0, row=5)

sorted_var = tk.StringVar()
sorted_label = tk.Label(textvariable=sorted_var, font="Inconsolata 14")
sorted_label.grid(column=1, row=5)


sort = tk.Button(command=sort_callback, text="Sort", font="Inconsolata 14")
sort.grid(column=0, row=6)

table = [
    ["-", N1, N2, N3],
    ["Рандомный массив", *random_res],
    ["Упорядоченный массив", *sorted_res],
    ["Обратно упорядоченный массив", *reversed_res],
]

gen_table(table, 7, 0)

root.mainloop()
