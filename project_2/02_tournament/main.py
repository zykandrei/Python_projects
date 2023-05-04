name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

first_day_list = []

for index, new_list in enumerate(name_list):
    if index % 2 == 0:
        first_day_list.append(new_list)
print('Первый день:', first_day_list)
