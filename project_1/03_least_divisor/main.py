def min_divider(numbers):
    divider = 1
    while divider <= numbers:
        divider += 1
        if numbers % divider == 0:  #очевидно -  первый делитель будет наименьшим
            print('Наименьший делитель, отличный от единицы: ', divider)
            break


number = int(input('Введите число: '))
min_divider(number)