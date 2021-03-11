import tkinter as tk
import random
from toolz.curried import map as cmap
from toolz import compose
from functools import partial
import timeit

# Functions and static

N1 = 10 ** 1
N2 = 10 ** 2
N3 = 10 ** 3

time = partial(timeit.timeit, number=1)

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


def yield_cells(rows, padding=2):
    col_lens = max_col_len(rows)
    formatters = ["{:" + str(cl) + "}" for cl in col_lens]
    for row in rows:
        for col, fmt in zip(row, formatters):
            text = ' '*padding + fmt.format(col) + ' '*padding
            cell = tk.Label(text=text, font="Inconsolata 12")
            yield cell


# return maximum len for each column
def max_col_len(rows):
    col_len = [0 for i in rows]
    n_rows = len(rows)
    n_cols = len(rows[0])
    for row in range(n_rows):
        for col in range(n_cols):
            col_len[col] = max(col_len[col], len(rows[row][col]))
    return col_len


def gen_table(rows, grid_start_row, grid_start_col):
    n_rows = len(rows)
    n_cols = len(rows[0])
    idx = 0
    for cell in yield_cells(rows):
        col = grid_start_col + idx % n_cols
        row = grid_start_row + idx // n_rows
        idx += 1
        cell.grid(
            column=col, row=row
        )


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


# Util functions:
def sort_time(arr):
    return time(lambda: barrier_sort(arr))


def serialize_int_list(arr):
    max_len_str = str(len(str(max(arr))))
    len_fmt = "{:" + max_len_str + "}"
    pipe = compose(" ".join, cmap(len_fmt.format))
    return pipe(arr)


# gen func is a generator for array to sort
def time_test(gen_func):
    arrays = map(gen_func, [N1, N2, N3])
    times = [sort_time(a) for a in arrays]
    return map("{:.3e}".format, times)


arr_small = random_arr(10)

# Init
root = tk.Tk()
root.title("Calculator")

unsorted_text = "Unsorted:  " + serialize_int_list(arr_small)
unsorted_label = tk.Label(text=unsorted_text, font="Inconsolata 14")
unsorted_label.grid(column=0, row=0)

sorted_text = "Sorted:    " + serialize_int_list(barrier_sort(arr_small))
sorted_label = tk.Label(text=sorted_text, font="Inconsolata 14")
sorted_label.grid(column=0, row=1)

table = [
    ["-", *map(str, [N1, N2, N3])],
    ["Рандомный массив", *time_test(random_arr)],
    ["Упорядоченный массив", *time_test(sorted_arr)],
    ["Обратно упорядоченный массив", *time_test(reversed_sorted_arr)],
]


gen_table(table, 2, 0)

root.mainloop()
