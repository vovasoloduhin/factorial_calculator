def factorial(n):
    if n < 0:
        return "Факторіал для від'ємних чисел не існує."

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


number = int(input("Введіть число: "))
print(f"Факторіал числа {number} = {factorial(number)}")