"""
## 3
Из заданного множества точек на плоскости выбрать
две различные точки так, чтобы окружности заданного радиуса с центрами
на этих точках содержали внутри себя одинаковое колличество точек.

Дать графическое изображение реззультатов
"""

import tkinter as tk
from dataclasses import dataclass
from typing import Optional
from visualizer import Visualizer


@dataclass
class Point:
    x: int
    y: int


class PointManager:
    def __init__(self):
        self.id = 1
        self.entries = []

    def add(self):
        self.entries.append(PointField(self.id, self))
        self.id += 1
        self.show()

    def add_initialized(self, p: Point):
        self.add()
        self.entries[-1].set(p)

    def delete(self, id: int):
        index = 0
        k = 0
        for idx, i in enumerate(self.entries):
            if i.n == id:
                index = idx
            else:
                i.set_n(k)
                k += 1
        self.entries.pop(index)
        self.id -= 1

    def show(self):
        for i in self.entries:
            i.display()

    def get(self):
        for i in self.entries:
            yield i.get()


class PointField:
    n_label: tk.Label
    id_var: tk.StringVar
    x_label: tk.Label
    y_label: tk.Label
    y_input: tk.Entry
    x_input: tk.Entry
    x_var: tk.StringVar
    y_var: tk.StringVar
    delete_btn: tk.Button

    def __init__(self, n: int, manager: PointManager):
        self.n = n
        self.manager = manager
        self.id_var = tk.StringVar()
        self.id_var.set(f"id: {n}")
        self.n_label = tk.Label(textvariable=self.id_var, font="Inconsolata 14")
        self.x_label = tk.Label(text="x:", font="Inconsolata 14")
        self.x_var = tk.StringVar()
        self.x_input = tk.Entry(textvariable=self.x_var, font="Inconsolata 14")
        self.y_label = tk.Label(text="y:", font="Inconsolata 14")
        self.y_var = tk.StringVar()
        self.y_input = tk.Entry(textvariable=self.y_var, font="Inconsolata 14")
        self.delete_btn = tk.Button(
            text="x", font="Inconsolata 14", command=self.delete
        )

    def display(self):
        self.n_label.grid(row=self.n, column=0)
        self.x_label.grid(row=self.n, column=1)
        self.x_input.grid(row=self.n, column=2)
        self.y_label.grid(row=self.n, column=3)
        self.y_input.grid(row=self.n, column=4)

        self.delete_btn.grid(row=self.n, column=5)

    def get(self) -> Optional[Point]:
        try:
            x = int(self.x_var.get())
            y = int(self.y_var.get())
            return Point(x, y)
        except ValueError:
            return None

    def set(self, p: Point):
        self.x = p.x
        self.y = p.y
        self.x_var.set(str(p.x))
        self.y_var.set(str(p.y))

    def set_n(self, n: int):
        self.n = n
        self.id_var.set(f"id: {n}")

    def delete(self):
        for el in [
            self.n_label,
            self.x_label,
            self.y_label,
            self.x_input,
            self.y_input,
            self.delete_btn,
        ]:
            el.destroy()
        self.manager.delete(self.n)


class PointManagerWindow:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("PointManager")
        self.manager = PointManager()

        self.get_btn = tk.Button(self.master, text="print_points", command=lambda: print(list(self.manager.get())))
        self.get_btn.grid(row=0, column=0)

        self.add_btn = tk.Button(self.master, text="add_point", command=self.manager.add)
        self.add_btn.grid(row=0, column=1)

        self.update_btn = tk.Button(self.master, text="redraw points", command=self.redraw_points)
        self.update_btn.grid(row=0, column=1)

        self.open_visualizer()
    
    def open_visualizer(self):
        self.visualizer_window = tk.Toplevel(self.master)
        self.visualizer = Visualizer(self.visualizer_window, self.manager)
    
    def redraw_points(self):
        self.visualizer.redraw_points()
