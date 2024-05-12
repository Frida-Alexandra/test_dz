# Задание «Квадратное уравнение»


def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b**2 - 4 * a * c


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    d = discriminant(a, b, c)
    if d < 0:
        return "корней нет"
    elif d == 0:
        result = (-b) / (2 * a)
        return result
    else:
        result1 = (-b + (d**0.5)) / (2 * a)
        result2 = (-b - (d**0.5)) / (2 * a)
        return (result1, result2)


if __name__ == "__main__":
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)
