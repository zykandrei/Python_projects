def coordinates(x, y, r):
    if abs(x) > r or abs(y) > r:
        print('\nМонетки в области нет.')
    else:
        print('\nМонетка где-то рядом.')


point_x = float(input('Введите координату x: '))
point_y = float(input('Введите координату y: '))
circle_r = float(input('Введите радиус: '))
coordinates(point_x, point_y, circle_r)