shift = int(input('Сдвиг:'))
initial_list = []
new_list = []
count_num = int(input('Kол-во элементов списка: '))
for _ in range(count_num):
    initial_list.append(int(input('Введите элемент: ')))

elem = len(initial_list) - shift

for i in range(elem, count_num):
    new_list.append(initial_list[i])
for j in range(0, elem):
    new_list.append((initial_list[j]))
print('Изначальный список: ', initial_list)
print('Сдвинутый список: ', new_list)