animals = 'dog'
print(animals == 'cat')
alien_color = 'green'
if alien_color =='green':
    print('you have got 5 points')
alien_color = 'red'
if alien_color =='green':
    print('you have got 5 points')
alien_color = 'green'
if alien_color !='green':
    print('you have got 5 points for killing the alien.')
else :
    print('you have got 10 points')
alien_color = 'red'
if alien_color =='green':
    print('you have got 5 points ')
elif alien_color =='yellow' : 
    print('you have got 10 points')
else:
    print('you have got 15 points')
age = 99
if age<2:
    print("he is a baby.")
elif age<4:
    print('he is a toddler.') 
elif age<13:
    print('he is a child.')
elif age<20:
    print('he is a teenager.')
elif age<65:
    print('he is an adult.')
else :
    print('he is an elder.')
favourite_fruits=['apple' , 'mango',  'peach']
if 'apple' in favourite_fruits :
    print('You really like apple!')
if 'mango' in favourite_fruits :
    print('You really like mango!')
if 'peach' in favourite_fruits :
    print('You really like peach!') 
if 'orange' in favourite_fruits :
    print('You really like orange!')
if 'banana' in favourite_fruits :
    print('You really like banana!')
users=[]
for user in users:
    if user =='admin':
        print('Hello admin, would you like to see a status report?')
    else :
        print('hello '+ user + ', thank you for logging in again.')
print('\n')
if users :
    for user in users:
        if user =='admin':
            print('Hello admin, would you like to see a status report?')
        else :
            print('hello '+ user + ', thank you for logging in again.')
else :
    print('We need to find some users!')
print('\n')
current_users=['mike' , 'john' , 'adMin', 'Eric', 'black']
new_users =['lily' , 'lucy', 'tom','Admin','Eric' ]
current_users_lower = [user.lower() for user in current_users] #精髓 创建新的小写列表
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(new_user + ' has been uesd, you need to choose a new username') 
    else:
        print(new_user + ' has not been used.')
numbers=list(range(1,10))
for number in numbers:
    if number == 1 :
        print(str(number) + 'st')
    elif number == 2 :
        print(str(number) + 'nd')
    elif number == 3 :
        print(str(number)+ 'rd')
    else:
        print(str(number)+ 'th')
