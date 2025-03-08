from Octagon import Octagon

# Создание объекта
octagon = Octagon(5)

# Вывод параметров
print("1. Описанная окружность:")
print(f"   Радиус: {octagon.circumscribed_circle_radius():.2f}")  # ≈ 6.47
print(f"   Площадь: {octagon.circumscribed_circle_area():.2f}\n")  # ≈ 131.27

print("2. Вписанная окружность:")
print(f"   Радиус: {octagon.inscribed_circle_radius():.2f}")  # ≈ 4.83
print(f"   Площадь: {octagon.inscribed_circle_area():.2f}\n")  # ≈ 73.24

print("3. Параметры октагона:")
print(f"   Площадь: {octagon.octagon_area():.2f}")  # ≈ 120.71
print(f"   Периметр: {octagon.octagon_perimeter()}\n")  # 40

# Отрисовка
octagon.draw()