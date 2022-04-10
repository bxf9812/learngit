import requests
from bs4 import BeautifulSoup
bs = BeautifulSoup(open('Python爬虫入门教程：超级简单的Python爬虫教程.html', encoding='utf-8'), 'lxml')
data = bs.find_all
# print(data)

url = 'https://www.cnblogs.com/geo-will/p/10468253.html'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text,'lxml')
soup.encode = 'utf-8'
a = soup.title
print(a)