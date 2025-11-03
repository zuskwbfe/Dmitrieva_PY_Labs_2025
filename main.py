from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square

def main():
    circle = Circle(1, "белого")
    rectangle = Rectangle(1, 1, "синего")
    square = Square(1, "красного")
    print(circle)
    print(rectangle)
    print(square)

if __name__ == "__main__":
    main()
