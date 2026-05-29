from datetime import datetime

# first_name=input('Enter your first name: ')
# last_name=input('Enter your last name: ')
# #formatter
# print(f'Hello {first_name} {last_name}')
#type conversion
age=45
# print('your age is' +str(age))
# current_date=datetime.now()
# print('today date is :' +str(current_date))
zero=0
try:
    print(age/zero)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
finally:
    print('clean up')

