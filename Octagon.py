import math
import matplotlib.pyplot as plt
import numpy as np

class Octagon:
    def init(self, side):
        self.side = side  # Длина стороны октагона
        self.angle = 135  # Угол между сторонами (константа)

    # Методы для радиусов окружностей
    def circumscribed_circle_radius(self):
        # Радиус описанной окружности: R = (a/2) * sqrt(4 + 2√2)
        return (self.side / 2) * math.sqrt(4 + 2 * math.sqrt(2))

    def inscribed_circle_radius(self):
        # Радиус вписанной окружности: r = (a/2) * (1 + √2)
        return (self.side / 2) * (1 + math.sqrt(2))

    # Методы для площадей
    def circumscribed_circle_area(self):
        return math.pi * (self.circumscribed_circle_radius() ** 2)

    def inscribed_circle_area(self):
        return math.pi * (self.inscribed_circle_radius() ** 2)

    # Площадь и периметр октагона
    def octagon_area(self):
        return 2 * (1 + math.sqrt(2)) * (self.side ** 2)

    def octagon_perimeter(self):
        return 8 * self.side

    # Визуализация
    def draw(self):
        center_x, center_y = 0, 0  # Центр в (0, 0)
        R = self.circumscribed_circle_radius()
        r = self.inscribed_circle_radius()

        # Координаты вершин октагона
        angles = np.linspace(0, 2 * np.pi, 9)[:-1]
        x = center_x + R * np.cos(angles)
        y = center_y + R * np.sin(angles)

        # Отрисовка октагона
        plt.plot(np.append(x, x[0]), np.append(y, y[0]), label="Octagon", color="blue", linewidth=2)

        # Отрисовка описанной окружности
        circle_angles = np.linspace(0, 2 * np.pi, 100)
        cx = center_x + R * np.cos(circle_angles)
        cy = center_y + R * np.sin(circle_angles)
        plt.plot(cx, cy, label="Circumscribed Circle", color="green", linestyle="--")

        # Отрисовка вписанной окружности
        ix = center_x + r * np.cos(circle_angles)
        iy = center_y + r * np.sin(circle_angles)
        plt.plot(ix, iy, label="Inscribed Circle", color="red", linestyle=":")

        # Настройки графика
        plt.gca().set_aspect("equal")
        plt.title("Октагон с окружностями")
        plt.xlabel("Ось X")
        plt.ylabel("Ось Y")
        plt.legend()
        plt.grid(True)
        plt.show()