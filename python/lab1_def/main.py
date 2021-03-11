import tkinter as tk

root = tk.Tk()
root.title("Def 1")

input1 = tk.StringVar()
input2 = tk.StringVar()
result = tk.StringVar()


def tri_sub(n1, n2):
    if n1 - n2 < 0:
        return 3 + n1 - n2, 1
    return n1 - n2, 0


def tri_sub_num(str1: str, str2: str):
    res = []
    carry_over = 0
    for n1, n2 in reversed(list(zip(str1, str2))):
        n1, n2 = int(n1), int(n2)
        n1, carry1 = tri_sub(n1, carry_over)
        sub_res, carry2 = tri_sub(n1, n2)
        carry_over = carry1 + carry2
        res.append(str(sub_res))
    res = "".join(reversed(res))
    res = res.lstrip("0")
    return res


def first_gtr(str1, str2):
    for n1, n2 in zip(str1, str2):
        if n1 == n2:
            continue
        if int(n1) > int(n2):
            return True
        else:
            return False
    return False


def make_strings_eq_len(str1, str2):
    if len(str1) == len(str2):
        return str1, str2
    if len(str1) < len(str2):
        return str1.rjust(len(str2), "0"), str2
    else:
        return str1, str2.rjust(len(str1), "0")


def calc():
    str1 = input1.get()
    str2 = input2.get()
    str1, str2 = make_strings_eq_len(str1, str2)
    first_greater = first_gtr(str1, str2)
    if first_greater:
        res = tri_sub_num(str1, str2)
    else:
        res = "-" + tri_sub_num(str2, str1)
    result.set(res)


tk.Label(text="Nubmer 1  ", font="Inconsolata 14").grid(column=0, row=0)

input1_entry = tk.Entry(root, width=16, textvariable=input1, font="Inconsolata 16")
input1_entry.grid(column=1, row=0)


input2_entry = tk.Entry(root, width=16, textvariable=input2, font="Inconsolata 16")
input2_entry.grid(column=1, row=1)

tk.Label(text="Nubmer 2  ", font="Inconsolata 14").grid(column=0, row=1)

calc_button = tk.Button(text="Calc", font="Inconsolata 14", command=calc)
calc_button.grid(column=0, row=2)

result_label = tk.Label(textvariable=result, font="Inconsolata 14")
result_label.grid(column=1, row=2)

root.mainloop()
