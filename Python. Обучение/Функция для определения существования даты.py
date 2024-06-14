def date(day=31, month=12, year=1999):
    if year in range(-30000, 30001):
        if month in range(1, 13):
            if month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32):
                return 'Такая дата существует'
            elif month in [4, 6, 9, 11] and day in range(1, 31):
                return 'Такая дата существует'
            elif month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and day in range(1, 30):
                return 'Такая дата существует'
            elif month == 2 and day in range (1, 29):
                return 'Такая дата существует'
            else:
                return 'Такой даты не существует'
        else:
            return 'Такой даты не существует'
    else:
        return 'Такой даты не существует'

print(date(day=28, month=2, year=2023))