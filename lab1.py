import sys
import math

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index] # чтение из консоли python3 lab1.py a b c
    except:
        print(prompt)
        coef_str = input()
    try:
        coef = float(coef_str)
        return coef, 1
    except ValueError:
        print('Ошибка: введите число в правильном формате.')
        return 0, 0

def get_roots(a, b, c):
    if a == 0.0:
        print('Это не квадратное уравнение.')
        return []
    result = []
    D = b ** 2 - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result.append(root1)
        result.append(root2)
    return result


def main():
    flag = 0
    while True:
        a, is_correct1 = get_coef(1, 'Введите коэффициент А (действительное число, пример: 3.14):')
        b, is_correct2 = get_coef(2, 'Введите коэффициент B (действительное число, пример: 3.14):')
        c, is_correct3 = get_coef(3, 'Введите коэффициент C (действительное число, пример: 3.14):')
        if not (is_correct1 and is_correct2 and is_correct3):
            print('Введены некорректные значения, повторите попытку.')
            continue
        if a == 0:
            print("Коэффициент A не может быть равен 0 для квадратного уравнения")
            continue
        roots = get_roots(a,b,c)
        len_roots = len(roots)
        if len_roots == 0:
            print('Нет корней')
        elif len_roots == 1:
            print('Один корень: {}'.format(roots[0]))
        elif len_roots == 2:
            print('Два корня: {} и {}'.format(roots[0], roots[1]))

        break

if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 -5 -36
