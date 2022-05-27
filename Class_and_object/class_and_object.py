class Rectangle:
    default_color = "green"

    def __init__(self, width, height):
        self.width = width
        self.height = height

r1 = Rectangle(1, 2)
r2 = Rectangle(10, 20)
print(r1.default_color)
print(r2.default_color)
#Через экземпляр можно поменять статический атрибут для конкретного объекта класса r1.
r1.default_color = "blue"
print(r1.default_color)
print(r2.default_color)
#А сам статический атрибут класса, нельзя поменять
print(Rectangle.default_color)
