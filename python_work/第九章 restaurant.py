# 9-1
class Restaurant() :
    '''餐馆'''
    def __init__(self, restaurant_name, cuisine_type) :
        """初始化name和type"""
        self.restaurant_name = restaurant_name.upper()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self) :
        """描述餐厅"""
        print(f'The restaurant name is {self.restaurant_name} . ')
        print(f'The cuisine type is {self.cuisine_type} .')
    def open_restaurant(self) :
        """正在营业"""
        print(f'The {self.restaurant_name} is now open.\n')
    def set_number_served(self, number) :
        '''设置就餐人数'''
        self.number_served = number
    def increment_number_served(self, everyday) :
        '''增加就餐人数'''
        self.number_served += everyday

A_res = Restaurant("kfc" , "chicken")
print(A_res.restaurant_name)
print(A_res.cuisine_type)
A_res.describe_restaurant()
A_res.open_restaurant()
# 9-2
B_res = Restaurant('pizza hut' , 'pizza')
B_res.describe_restaurant()
B_res.open_restaurant()
# 9-4
print(A_res.number_served)
A_res.number_served = 34
print(A_res.number_served)
A_res.set_number_served(50)
print(A_res.number_served)
A_res.increment_number_served(15)
print(A_res.number_served)
# 9-6
class IceCreamStand(Restaurant): 
    '''子类冰淇淋'''
    def __init__(self, restaurant_name, cuisine_type):
        '''继承restaurant'''
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    def show_flavors(self): 
        '''显示各种冰淇淋'''
        print('we have the following flavors: ')
        for fla in self.flavors :
            print(f' {fla} ')
C_ice = IceCreamStand('SUKIYA', 'gyudon')
C_ice.flavors = ['milk', 'honey', 'chocolate', 'vanilla', 'coffee']
C_ice.describe_restaurant()
C_ice.show_flavors()