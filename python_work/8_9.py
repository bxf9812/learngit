def show_messages(msg) :
    for ms in msg :
        print(ms.title())
def send_messages(send , sent) :
    while send :
        ss = send.pop()
        print(ss)
        sent.append(ss)
mess = ['hello' , 'hi' ,'how are you']
sent_messages=[]
show_messages(mess)
send_messages(mess[:] , sent_messages)
print(mess)
print(sent_messages)
def make_sand(*toppings):
    print('\nyou have made a sandwich with the following toppings: ')
    for topping in toppings :
        print(topping + ".")
make_sand('asd')
make_sand('qwe' , 'zxc' , 'fgh')
make_sand('sdf' , 'qawer' )
def car_maker(maker , type , **info):
    make_car ={}
    make_car['maker'] = maker.title()
    make_car['type'] = type.title()
    for k,v in info.items():
        make_car[k] = v
    return make_car
car = car_maker('subaru', 'outback', color='blue', tow_package=True)
print(car)
car1 = car_maker('audi' , 'suv' ,size = 'large' , color = 'red' ,year = 10)
print(car1)
