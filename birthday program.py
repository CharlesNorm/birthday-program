import datetime
import calendar
months = [
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december'
]
endings = ['st', 'nd', 'rd', ] + 17*['th'] + ['st', 'nd', 'rd'] + 7*['th'] + ['st']
year = input('ENTER CURRENT YEAR; ')
month = input('ENTER BIRTH MONTH(1-12); ')
day = input('ENTER BIRTHDAY(1-31); ')
age = int(input('ENTER YOUR AGE; '))
Birth_year = year - age
Birth_date = calendar.weekday(Birth_year, month, day)
date = calendar.day_name[Birth_date]
my_month = datetime.date(int(year), int(month), int(day))
b = int(month) - 1
a = int(day) - 1
print('you were born on' ' ' + date + ',' + my_month.strftime("%d") + endings[int(a)] + ' ' + months[int(b)] + ' ' + str(Birth_year))
