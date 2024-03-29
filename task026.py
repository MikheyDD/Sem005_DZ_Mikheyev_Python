# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def pow_nums(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return a * pow_nums(a, b - 1)


print(pow_nums(3, 5))


