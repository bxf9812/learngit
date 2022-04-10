def display_message() :
    """在本章学的是什么"""
    print("function")
display_message()
def favorite_book(title):
    """喜欢的图书"""
    print('One of my favorite books is ' + title.title() + ' .') 
favorite_book('xiyouji')
def make_shirt(size='large', word='I love Python' ) :
    """T 恤"""
    print('\nThe size of the t-shirt is ' + size + " .")
    print('Those words are on the t-shirt : ' + word + ' .')
make_shirt()
make_shirt('medium')
make_shirt(word='asshole')
def describe_city(name  , country = 'Iceland')  :
    '''描述城市'''
    print('\n' + name.title() + ' is in ' + country.title() + ' .')
describe_city('Reykjavik')
describe_city('suzhou' , 'china')
describe_city('tokyo' , 'japan')
def city_country(name , country) :
    """城市名"""
    aaa= name.title() + ' , ' + country.title()
    return aaa
print(city_country('hangzhou' , 'china'))
print(city_country('london' , 'the uk'))
print(city_country('oosaka' , 'japan'))
def make_album(singer , album_name , number = 0) :
    """专辑"""
    album= {
        'singer' : singer.title() , 
        'name' : album_name.title() , 
        }  
    if number :
        album['number'] = number
    return album
a1 = make_album('ask' , 'qqq' , 5)
print(a1)
a2 = make_album('john' , 'waxd' , 2)
print(a2)
a3 = make_album('zxc' , 'loiuj')
print(a3)
while True :
    print('please enter the singer: ')
    print('please enter the album: ')
    print('enter q to quit. ')
    singer = input('singer')
    if singer=='q':
        break
    album = input('album')
    if album =='q':
        break
    sa = make_album(singer, album)
    print(sa)