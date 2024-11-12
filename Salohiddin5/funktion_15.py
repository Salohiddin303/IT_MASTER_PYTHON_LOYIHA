def calculations(a, b):
    summa = a + b
    diff = a - b
    mul = a * b
    div = a / b
    return summa, diff, mul, div
num1, num2 = int(input('num1= ')), int(input('num2= '))
summa, diff, mul, div = calculations (num1, num2)
print(
    f'Сумма: {summa}\n'
    f'Разница: {diff}\n'
    f'Произведение: {mul}\n'
    f'Результат деления: {div:.2f}\n'
    )


