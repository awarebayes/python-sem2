import tkinter as tk
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


class Visualizer:
    def __init__(self, master, point_manager):
        self.manager = point_manager
        self.master = master
        self.c = tk.Canvas(self.master, width=500, height=500, bg="white")
        self.c.pack()
        self.c.bind("<Button-1>", self.handle_click)

    def handle_click(self, event):
        self.manager.add_initialized(Point(event.x, event.y))
        self.redraw_points()

    def redraw_points(self, clear=True):
        if clear:
            self.c.delete("all")
        points = self.manager.get()
        points = filter(lambda x: x, points)
        for p in points:
            self.c.create_oval(p.x, p.y, p.x, p.y, width=2, fill="black")
