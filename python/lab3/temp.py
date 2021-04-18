# 24 % 9 + 1 = 7

# Метод простых итераций

# %%

import numpy as np

N_MAX = 10_000

untils = {
    "f": lambda g, f, x, eps: abs(f(x)) > eps,
    "g": lambda g, f, x, eps: abs(g(x) - x) > eps,
}


def iter_root(g, f, x, eps, until):
    n = 0
    while until(g, f, x, eps):
        x = g(x)
        n += 1
        if n > N_MAX:
            break
    return x, n


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
        root, n_iter = iter_root(g_x, f_x, middle, eps, until)

        yield root_n, (st, en), root, f_x(root), n_iter

        root_n += 1


# %%

a, b, s = -5, 5, 0.5
for info in root_info(a, b, s, 0.01, untils["f"]):
    print(info)


# %%

table = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

r = 2
c = 5

i = 0
for i in range(10):
    print(i // c, i % c)

# %%

import numpy as np

np.roll(np.arange(-10, 10, 0.2), 3)
# %%


def extemum(arr):
    for i in range(1, len(arr - 1)):
        if arr[i - 1] > arr[i] < arr[i + 1] or arr[i - 1] < arr[i] > arr[i + 1]:
            yield i


# %%

np.take(nбббббббббp.array([1, 2, 3, 4, 5]), [1, 2])
# %%
