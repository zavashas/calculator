import math
while True:
    print('Выберите операцию:')
    print('1. Сложение')
    print('2. Вычитание')
    print('3. Умножение')
    print('4. Деление')
    print('5. Возведение в степень')
    print('6. Квадратный корень')
    print('7. Факториал')
    print('8. Синус')
    print('9. Косинус')
    print('10. Тангенс')
    print('0. Выход')

    operation = input('Введите номер операции: ')

    if operation == '0':
        break

    if operation in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        if operation in ('6', '7', '8', '9', '10'):
            a = float(input('Введите число: '))
        else:
            a = float(input('Введите первое число: '))
            b = float(input('Введите второе число: '))

        if operation == '1':
            result = a + b
        elif operation == '2':
            result = a - b
        elif operation == '3':
            result = a * b
        elif operation == '4':
            if b == 0:
                result = a / b
            else:
                print('Ошибка: деление на ноль')
                continue
        elif operation == '5':
            result = a ** b
        elif operation == '6':
            if a >= 0:
             result = math.sqrt(a)
            else:
             print('Ошибка: отрицательное число под корнем')
        elif operation == '7':
            if a >= 0:
             result = math.factorial(int(a))
            else:
             print('Ошибка: факториал определен только для неотрицательных целых чисел')
        elif operation == '8':
            result = math.sin(a)
        elif operation == '9':
            result = math.cos(a)
        elif operation == '10':
            result = math.tan(a)

        print('Результат:', result)
    else:
        print('Ошибка: неверный выбор операции')

