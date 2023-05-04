films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

count_films = int(input('Сколько фильмов хотите добавить? '))
favorite_list = []

for _ in range(count_films):
    name_film = input('Введите название фильма: ').title()
    if name_film in films:
        favorite_list.append(name_film)
    else:
        print(f'Ошибка: фильма: {name_film} у нас нет :(')
result = ', '.join(favorite_list)

print("Ваш список любимых фильмов: ", result)