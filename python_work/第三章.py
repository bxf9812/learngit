fruit=['apple' , 'banana', 'mango', 'orange', 'peach']
print(fruit)
print(fruit[3].title())
print(fruit[-1])
msg="my favourite fruit is " + fruit[2].title() +"."
print(msg)
fruit=['apple' , 'banana', 'mango', 'orange', 'peach']
print(fruit)
fruit[0]='pear'
print(fruit)
fruit=['apple' , 'banana', 'mango', 'orange', 'peach']
print(fruit)
fruit.append('watermelon')
print(fruit)
fruit=['apple' , 'banana', 'mango', 'orange', 'peach']
fruit.insert(1,'pear')
print(fruit)
del fruit[1]
print(fruit)
fruit.pop()
print(fruit)
fruit=['apple' , 'banana', 'mango', 'orange', 'peach']
favourite_fruit=fruit.pop(2)
print("my favourite fruit is " + favourite_fruit.title() + ".")
print(fruit)
fruit=['apple' , 'banana', 'mango', 'orange', 'peach']
fruit.remove("apple")
print(fruit)
fruit=['banana' , 'apple' ,  'peach', 'mango', 'orange']
fruit.sort()
print(fruit)
fruit=['banana' , 'apple' ,  'peach', 'mango', 'orange']
fruit.sort(reverse=True)
print(fruit)
fruit=['banana' , 'apple' ,  'peach', 'mango', 'orange']
print("\nfruit list")
print(fruit)
print(sorted(fruit))
fruit.reverse()
print(fruit)
print(len(fruit))