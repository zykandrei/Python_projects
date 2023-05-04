def years(first_y, second_y):
    string_1 = ''
    string_2 = ''
    count = 1
    for year in range(first_y, second_y + 1):
        for number in str(year):
            if number in string_1:
                count += 1
                string_2 += number
                if count == 3:
                    if string_1 != string_2 and int(string_2) % 11 == 0:
                        print(year)
            else:
                string_1 += number
        count = 1
        string_1 = ''
        string_2 = ''


first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))
print(f'\nГоды от {first_year} до {second_year} с тремя одинаковыми цифрами: ')
years(first_year, second_year)