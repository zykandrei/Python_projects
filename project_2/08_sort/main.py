
initial_list = []
count_num = int(input('Kол-во элементов списка: '))
for _ in range(count_num):
    initial_list.append(int(input('Введите элемент: ')))
print('Изначальный список: ', initial_list)

for i_min in range(len(initial_list)):
    for curr in range(i_min, len(initial_list)):
        if initial_list[curr] < initial_list[i_min]:
            initial_list[curr], initial_list[i_min] = initial_list[i_min], initial_list[curr]
print('Отсортированный список: ', initial_list)
