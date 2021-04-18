R = ["F", "A", "T", "O", "C", "L"]

ind = R.index


def cmp_str_gtr(s1, s2):
    if len(s1) < len(s2):
        s1 += R[0] * (len(s1) - len(s2))
    elif len(s2) < len(s1):
        s2 += R[0] * (len(s2) - len(s1))
    for i1, i2 in zip(s1, s2):
        if ind(i1) < ind(i2):
            return False
    return True


def cmp_gtr(n1, n2):
    if isinstance(n1, str) and isinstance(n2, str):
        return cmp_str_gtr(n1, n2)
    elif isinstance(n1, str) and isinstance(n2, int):
        return False
    elif isinstance(n2, str) and isinstance(n1, int):
        return True
    else:
        return n1 > n2


def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            if cmp_gtr(arr[i], arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def sort_arr(arr):
    strings = list(filter(lambda x: isinstance(x, str), arr))
    nums = list(filter(lambda x: isinstance(x, int), arr))
    strings_sorted = sort(strings)
    nums_sorted = sort(nums)
    return strings_sorted + nums_sorted


def apply_int(arr):
    for i in arr:
        try:
            yield int(i)
        except:
            yield i


def stringify(arr):
    for i in arr:
        if not isinstance(i, str):
            yield str(i)
        else:
            yield i


def callback():
    inp = inp_var.get().split()
    s = sort(list(apply_int(inp)))
    res_var.set(" ".join(list(stringify(s))))


import tkinter as tk

# Init
root = tk.Tk()
root.title("Calculator")


inp_var = tk.StringVar()
res_var = tk.StringVar()

l = tk.Label(text=f"Input", font="Inconsolata 14")
l.grid(row=0, column=0)

e = tk.Entry(textvariable=inp_var, font="Inconsolata 14")
e.grid(row=0, column=1, columnspan=2)

b = tk.Button(text="Sort", command=callback, font="Inconsolata 14")
b.grid(row=1, column=0)

r = tk.Label(textvariable=res_var, font="Inconsolata 14")
r.grid(row=2, column=0, columnspan=2)

root.mainloop()
