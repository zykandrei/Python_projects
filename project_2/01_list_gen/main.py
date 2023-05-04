number = int(input('Введите число: '))

num_list = []
for numbers in range(1, number + 1):
    if numbers % 2 == 1:
        num_list.append(numbers)

print(f'Список из нечётных чисел от одного до {number}: {num_list}')