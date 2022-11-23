#Age_Calculator
import datetime
print('Welcome to my age calculator!!!')
users_year_of_birth = int(input('What is your year of birth? '))
users_month_of_birth = int(input('What is your month of birth? '))
users_day_of_birth = int(input('What is your day of birth? '))

print('You are :', datetime.date.today().year - users_year_of_birth, 'yrs',datetime.date.today().month - users_month_of_birth, 'month',
        datetime.date.today().day - users_day_of_birth, 'days old')