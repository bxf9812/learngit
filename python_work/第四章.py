fruits=['apple' , 'banana', 'mango', 'orange', 'peach']
for fruit in fruits:
    print("I like " + fruit.title() + ".")
    print("I really love " + fruit.title() + '.\n')
print("I really like fruit.")
numbers=[value for value in range(1,21)]
print(numbers)
for shuzi in list(range(1,21)):
    print(shuzi)
print(list(range(1,21,2)))
suuji=list(range(1,1000001))
print(max(suuji))
print(min(suuji))
print(sum(suuji))
number=(list(range(3,31,3)))
for numbers in number:
    print(numbers)
cube=[value**3 for value in range(1,11)]
print(cube)
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
print(cubes)
fruits=['apple' , 'banana', 'mango', 'orange', 'peach']
friend_fruits=fruits[:]
fruits.append('pear')
friend_fruits.append('watermelon')
print('my favourite fruits are: ')
for fruit in fruits:
    print(fruit)
print("\nmy friend's favourite fruits are: ")
for fruit in friend_fruits:
    print(fruit)
foods=('meat' , 'pork' , 'carrot' , 'chicken' , 'duck')
print('\n')
for food in foods :
    print(food)
foods=('meat' , 'pork' , 'carrot' , 'vagetable' , 'fish')
print('\n')
for food in foods :
    print(food)
