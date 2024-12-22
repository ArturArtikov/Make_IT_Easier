def date(d, m, y):
    if y >= -30000 and y <= 30000:
        if m in ['January', 'February', 'March', 'April', 'May', 'June', \
        'July', 'August', 'September', 'October', 'November', 'December']:
            
            
            if m in ['January', 'March', 'May', 'June', 'July', 'August', 'October', 'December'] and (d >= 1 and d < 32):
                return 'Такая дата существует'
            elif m in ['April', 'June', 'September', 'November'] and (d >= 1 and d < 31):
                return 'Такая дата существует'
            elif m == 'February' and ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0) and (d >= 1 and d < 30):
                return 'Такая дата существует'
            elif m == 'February' and not ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0) and (d >= 1 and d < 29):
                return 'Такая дата существует'
            else:
                return 'Такой даты не существует'


        else:
            return 'Такого месяца не существует'
    else:
        return 'Такого года не существует'


print(date(d=int(input('Введите число: ')), m=input('\nВведите месяц: '), y=int(input('\nВведите год: '))))