import math
import matplotlib.pyplot as plt
import numpy as np

class Octagon:
    def __init__(self, side):
        self.side = side
        self.angle = 135  # Угол октагона (константа)
        self.k = 1 + math.sqrt(2)  # Константа k

    # Методы для задания 2
    def circumscribed_circle_radius(self):
        return (self.side * self.k) / 2

    def circumscribed_circle_area(self):
        radius = self.circumscribed_circle_radius()
        return math.pi * (radius ** 2)

    def inscribed_circle_radius(self):
        return self.side / (2 * math.tan(math.pi / 8))

    def inscribed_circle_area(self):
        radius = self.inscribed_circle_radius()
        return math.pi * (radius ** 2)

    def octagon_area(self):
        return 2 * (self.side ** 2) * self.k

    def octagon_perimeter(self):
        return 8 * self.side

    # Метод для задания 3 (визуализация)
    def draw(self):
        angles = np.linspace(0, 2 * np.pi, 9)[:-1]  # 8 углов
        R = self.circumscribed_circle_radius()
        x = R * np.cos(angles)
        y = R * np.sin(angles)

        # Отрисовка октагона
        plt.plot(np.append(x, x[0]), np.append(y, y[0]), label="Octagon", color="blue", linewidth=2)

        # Отрисовка описанной окружности
        circle_angles = np.linspace(0, 2 * np.pi, 100)
        cx = R * np.cos(circle_angles)
        cy = R * np.sin(circle_angles)
        plt.plot(cx, cy, label="Circumscribed Circle", color="green", linestyle="--")

        # Отрисовка вписанной окружности
        r = self.inscribed_circle_radius()
        ix = r * np.cos(circle_angles)
        iy = r * np.sin(circle_angles)
        plt.plot(ix, iy, label="Inscribed Circle", color="red", linestyle=":")

        # Настройки графика
        plt.gca().set_aspect("equal")
        plt.title("Октагон с окружностями")
        plt.xlabel("Ось X")
        plt.ylabel("Ось Y")
        plt.legend()
        plt.grid(True)
        plt.show()