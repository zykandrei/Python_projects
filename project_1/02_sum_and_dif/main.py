def sum_number(numbers):
    global sum_numbers  #Присваиваем значение глобальной переменной внутри функции с помощью ключевого слова global
    while numbers > 0:
        num = numbers % 10
        sum_numbers = sum_numbers + num
        numbers = (numbers // 10)
    print('Сумма чисел: ', sum_numbers)


def digits_number(numbers):
    global digits   #Присваиваем значение глобальной переменной внутри функции с помощью ключевого слова global
    count_number = numbers
    while count_number > 0:
        digits += 1
        count_number = count_number // 10
    print('Количество цифр в числе: ', digits)


number = int(input('Введите число: '))
print()
sum_numbers = 0  # глоб. переменнaя
digits = 0  # глоб. переменнaя
sum_number(number)
digits_number(number)
print('Разность суммы и количество цифр: ', sum_numbers - digits)