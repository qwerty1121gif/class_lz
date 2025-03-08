from Octagon import Octagon

# Создание объекта
octagon = Octagon(5)

# Вывод параметров
print("1. Описанная окружность:")
print(f"   Радиус: {octagon.circumscribed_circle_radius():.2f}")
print(f"   Площадь: {octagon.circumscribed_circle_area():.2f}\n")

print("2. Вписанная окружность:")
print(f"   Радиус: {octagon.inscribed_circle_radius():.2f}")
print(f"   Площадь: {octagon.inscribed_circle_area():.2f}\n")

print("3. Параметры октагона:")
print(f"   Площадь: {octagon.octagon_area():.2f}")
print(f"   Периметр: {octagon.octagon_perimeter()}\n")

# Отрисовка
octagon.draw()