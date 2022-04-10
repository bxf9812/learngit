car = input('which car do you want to rent? ')
print('Let me see if I can find you a ' + car.title())
eat = input('how many people are you ? ')
eat = int(eat)
if eat > 8 :
    print('there is no table for you. ')
else :
    print('there is a table for you. ')
number = input('give me a number . ')
number = int(number)
if number % 10 == 0 :
    print('the number ' + str(number) + ' can be divisibled by 10. ')
else :
    print('the number ' + str(number) + ' can not be divisibled by 10. ')
x=1
while x<=5 :
    print(x)
    x += 1
message = '\nplease add your food: '
message += "\nenter quit to end the program. "
mes = ''
while mes != 'quit' :
    mes = input(message)
    if mes != 'quit' :
        print('we have add ' + mes + ' to you pizza.')
while True :
    age = input('tell me your age: ')
    if age == 'quit' :
        break 
    age = int(age)
    if age < 3 :
        print('free')
    elif age < 13 :
        print('$10')
    else :
        print('$15')
    
    