sandwich_orders = ['tuna' ,'pastrami' ,  'meat' ,'pastrami' , 'chicken' , 'pastrami'] 
finished_sandwiches = []
print('pastrami has sold out. ' )
while 'pastrami' in sandwich_orders :
    sandwich_orders.remove('pastrami')
while sandwich_orders :
    sandwichs = sandwich_orders.pop()
    print('I made your ' + sandwichs + ' .')
    finished_sandwiches.append(sandwichs)
print('these sandwichs have finished: ')
for sandwitches in finished_sandwiches :
    print(sandwitches)
response = {}
while True :
    name = input('what is your name ? ')
    result = input('If you could visit one place in the world, where would you go? ')
    response[name] = result 
    repeat = input('enter quit to quit the program. ')
    if repeat == 'quit':
        break
print('\n---- result----')
for k , v  in response.items():
    print(k.title() + ' would like to go to ' + v + ' .')