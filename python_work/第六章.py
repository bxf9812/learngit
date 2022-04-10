friend={
    'first_name' : 'su' , 
    'last_name' : 'zijun' , 
    'age' : '22' , 
    'city' : 'suzhou'
    }
print(friend['first_name'])
print(friend['last_name'])
print(friend['age'])
print(friend['city'])
people={'mike':5 ,'john' :15 ,'adMin' : 99, 'Eric' : 88, 'black' :66 }
number= people['john']
print(str(number))
glossary = {
 'string': 'A series of characters.',
 'comment': 'A note in a program that the Python interpreter ignores.',
 'list': 'A collection of items in a particular order.',
 'loop': 'Work through a collection of items, one at a time.',
 'dictionary': "A collection of key-value pairs.",
 'key': 'The first item in a key-value pair in a dictionary.',
 'value': 'An item associated with a key in a dictionary.',
 'conditional test': 'A comparison between two values.',
 'float': 'A numerical value with a decimal component.',
 'boolean expression': 'An expression that evaluates to True or False.',
 }
word = 'string'
print(word.title() + ': ' + glossary[word])
a=(20,50)
print(id(a))
a=(30,60)
print(id(a))
for k,v in glossary.items():
    print('\n' + k.title() + ': ' + v )
river= { 
    'nile': 'egypt' ,
    'changjiang': 'china',
    'amazon': 'south am', 
    }
for r,c in river.items():
    print('the ' + r.title() + ' runs through ' + c.title() + ' .')
for r in river.keys():
    print(r.title())
for c in river.values():
    print(c.title())
friend1={
    'first_name' : 'su' , 
    'last_name' : 'zhijiang' , 
    'age' : '23' , 
    'city' : 'hangzhou'
    }
friend2={
    'first_name' : 'su' , 
    'last_name' : 'zijun' , 
    'age' : '22' , 
    'city' : 'suzhou'
    } 
friend3={
    'first_name' : 'wang' , 
    'last_name' : 'ming' , 
    'age' : '42' , 
    'city' : 'shanghai'
    }
people = [friend1 , friend2 , friend3 ]
for person in people :
    full_name = person['first_name'].title() + " " + person['last_name'].title()
    age = person['age']
    city = person ['city'].title()
    print(full_name + ' is ' + age + ' years old, lives in ' + city + '.' )
favorite_places = {
    'a' : ['shanghai' , 'tokyo' , 'beijing'] ,
    'b' : ['suzhou' , 'kyoto' , 'london'] , 
    'c' : ['guangzhou' , 'taiwan' , 'hongkong'],    
    }
for k , v in favorite_places.items() : 
    print('\n' + k.title() + ' likes the following place: ' ) 
    for place in v :
        print('\t' + place.title())
people={'mike':[5,40,600] ,'john' :[33,66,55] ,'adMin' : [90,55555], 'Eric' : [233,2333,233333,233333], 'black' :[66,6,666,6666] }
for k,  v in people.items() :
    print('\n' + k.title() + ' likes the following number: ' ) 
    for number in v :
        print('\t' + str(number)) 
cities = {
    'suzhou' : {
        'country' : 'china' ,
        'population' : 10000000 ,
        'fact' : 'sdaknjdasajnhfasjnd'
        },
    'tokyo' : {
        'country' : 'japan' ,
        'population' : 12000000 ,
        'fact' : 'anime'
        },
    'new york' : {
        'country' : 'the usa' ,
        'population' : 20000000 ,
        'fact' : 'dsfsfsferf'
        },
    } 
print('Here are some informations about the following cities: ')
for k, v in   cities.items() :
    print('city name: ' + k.title())
    country = v['country'].upper()
    population = v['population']
    fact = v['fact']
    print('country: '+  country + '\n' + 'population: ' + str(population) + '\n' + 'fact: ' + fact + '\n' )
