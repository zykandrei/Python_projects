# MyProfile app
SEPARATOR = '------------------------------------------'
# user profile
name = ''
years_old = 0
phone = ''
email = ''
post_code = ''
post_address = ''
additional_inf = ''
# bank details
individual_number = ''
taxpayer_number = ''
checking_account = ''
bank_name = ''
individual_code = ''
correspondent_account = ''

def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, pc_parameter, pa_parameter, i_parameter):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif a_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'
    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    print('Индекс: ', pc_parameter)
    print('Адрес:  ', pa_parameter)
    if i:
        print('')
        print('Дополнительная информация:')
        print(i_parameter)
print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    years_old = int(input('Введите возраст: '))
                    if years_old > 0:
                        break
                    print('Возраст должен быть положительным')

                u_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for c_phone in u_phone:
                    if c_phone == '+' or ('0' <= c_phone <= '9'):
                        phone += c_phone

                email = input('Введите адрес электронной почты: ')

                u_post_code = input('Введите почтовый индекс: ')
                post_code = ''.join(c for c in u_post_code if c.isdecimal())

                post_address = input('Введите почтовый адрес (без индекса): ')
                i = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input bank details
                while True:
                    individual_number = input('Введите ОГРНИП: ')
                    count = 0
                    for i in individual_number:
                        count += 1
                    if count == 15:
                        break
                    else:
                        print('ОГРНИП должен содержать 15 цифр')
                taxpayer_number = input('Введите ИНН: ')
                while True:
                    checking_account = input('Введите расчетный счет: ')
                    count = 0
                    for i in checking_account:
                        count += 1
                    if count == 20:
                        break
                    else:
                        print('Расчетный счет должен содержать 20 цифр')

                bank_name = input('Введите название банка: ')
                individual_code = input('Введите БИК: ')
                correspondent_account = input('Введите корреспондентский счет: ')
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, years_old, phone, email, post_code, post_address, additional_inf)

            elif option2 == 2:
                general_info_user(name, years_old, phone, email, post_code, post_address, additional_inf)

                # print bank details
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП:', individual_number)
                print('ИНН:   ', taxpayer_number)
                print('Банковские реквизиты')
                print('Р/с:   ', checking_account)
                print('Банк:  ', bank_name)
                print('БИК:   ', individual_code)
                print('К/с:   ', correspondent_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
