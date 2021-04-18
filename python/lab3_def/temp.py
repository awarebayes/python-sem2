# y = sin x
# newton
# >> a, b (-2, 2)
# find root, no plot

# %%
import math as m

f = lambda x: m.sin(x)
f_dx = lambda x: m.cos(x)
eps = 0.001


def newton(a, b):
    x = (a + b) / 2
    while abs(f(x)) > eps:
        x = x - f(x) / f_dx(x)
    return x


# %%
