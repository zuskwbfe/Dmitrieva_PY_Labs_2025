import math
import sys

class  QuadraticEquation:
    def __init__(self, a = 0, b = 0, c = 0):
        self.a = a
        self.b = b
        self.c = c
        self.roots = []

    def calculate_roots(self):
        if self.a == 0:
            return

        D = self.b ** 2 - 4 * self.a * self.c

        if D == 0:
            root = -self.b / (2.0 * self.a)
            self.roots.append(root)
        if D > 0:
            sqD = math.sqrt(D)
            root1 = (-self.b + sqD) / (2.0 * self.a)
            root2 = (-self.b - sqD) / (2.0 * self.a)
            self.roots.append(root1)
            self.roots.append(root2)

    def get_roots_count(self):
        return len(self.roots)

    def get_roots(self):
        return self.roots.copy()

    def display_roots(self):
        count = self.get_roots_count()
        if count == 0:
            print('Нет корней')
        elif count == 1:
            print('Один корень: {}'.format(self.roots[0]))
        else:
            print('Два корня: {} и {}'.format(self.roots[0], self.roots[1]))

    @classmethod
    def get_coef(cls, index, prompt):
        try:
            coef_str = sys.argv[index]
        except:
            print(prompt)
            coef_str = input()
        try:
            coef = float(coef_str)
            return coef, 1
        except ValueError:
            print('Ошибка: введите число в правильном формате.')
            return None, 0

    @classmethod
    def create_from_input(cls):
        while True:
            a, is_correct1 = cls.get_coef(1, 'Введите коэффициент А:')
            b, is_correct2 = cls.get_coef(2, 'Введите коэффициент B:')
            c, is_correct3 = cls.get_coef(3, 'Введите коэффициент C:')

            if not (is_correct1 and is_correct2 and is_correct3):
                print("Введены некорректные значения, повторите попытку.")
                continue

            if a == 0:
                print("Коэффициент A не может быть равен 0 для квадратного уравнения")
                continue

            return cls(a, b, c)

    def __str__(self):
        return f"Уравнение: {self.a}x² + {self.b}x + {self.c} = 0"
