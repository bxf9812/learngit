import numpy as np
from numpy.core.numeric import ones_like
a = np.arange(10,18)
b = np.array((20,50,30,92))
print('format函数:\na={}\nb={}'.format(a,b))
print(f'f字符串:\na={a}\nb={b}')

tup = tuple(range(5))
print(f'tup:\n {tup}')
tup2arr = np.array(tup)
print(f'通过元组创建数组:\n{tup2arr}')

lst = list(range(15))
lst2 = np.array(lst)
lst3 = np.array(list(range(15)))
print(f'通过列表创建数组:\n{lst}\n{lst2}\n{lst3}')

x = np.linspace(1,10,3)
y = np.linspace(0,np.pi,7)
print(f'x={x}\ny={y}')

# 随机函数生成数组
print('随机函数生成数组')
np.set_printoptions(precision=2)
ar = np.random.rand(3,4) # (0,1)均匀分布
ar2 = np.random.randn(2,5) # N(0,1)分布
print(f'ar={ar}\nar2={ar2}\n')

# 生成特定范围内的随机整数
print('生成特定范围内的随机整数:')
a = np.random.randint(1,100,10) #(1,100)内5个随机数
b = np.random.randint(1,100,(2,3)) #2x3 数组
tup = tuple((10,10)) 
c = np.random.randint(1,200,(tup)) #10*10 数组
print(f'a={a}\nb={b}\nc={c}\n')

# 创建二维数组
d = np.arange(12).reshape(4,3)
e = np.arange(12).reshape(2,6)
print(f'd={d}\ne={e}')

# arange repeat tile reshape
a = np.arange(1,5,0.5)
b = np.repeat(a,3)
c = np.tile(a,3)
print(f'a={a}\nb={b}\nc={c}\n')

# 一些特殊的数组
a = np.ones(5)
b = np.ones((2,3))
c = np.zeros((3,3))
d = ones_like(c)
e = np.eye(5)
print(f'a={a}\nb={b}\nc={c}\nd={d}\ne={e}\n')

# 数据类型
a = np.full((3,4),True)
b = np.arange(5,dtype='float')
c = b.astype('int')
print(f'a={a}\nb={b}\nc={c}\n{a.dtype}\n{b.dtype}\n{c.dtype}\n')

# 数组的存取
b = np.arange(5,10)
print(f'{b}\n{b[1]}\n{b[-1]}\n{b[:2]}\n{b[1:3]}\n{b[[0,1,3]]}')
c = b
c[0] = 100
print(f'c={c}\nb={b}\nid_c={id(c)}\nid_b={id(b)}')
c = b.copy()
print(f'使用copy复制后：\nc={c}\nb={b}\nid_c={id(c)}\nid_b={id(b)}')

b = np.arange(12).reshape(3,-1)
print(b)
print(f'{b[1,2]}\n{b[1,1:3]}\n{b[1]}\n{b[:,1]}\n{b[1:3,1:4]}\n{b[1][2]}\n{b[1,2]}')
print(f'{b[[0,1,2],[3,2,1]]}\n') # ????

# 布尔索引
# 筛选出向量中小于给定值的元素
#np.random.seed(7)
b = np.random.randint(40,100,size=10)
c = b < 60
print(f'b={b}\nb中小于60的元素为:\n{b[c]}')
print(f'b中[60,75]间的元素为:\n{b[(b>=60) & (b<=75)]}')
print(f'显示<60  或 >90的数据:\n{b[(b<60) | (b>90)]}')
print(f'显示 >=60的数据:\n{b[~(b<60)]}') # ~非, 显示 >=60的数据

# 找出特定元素的位置
#np.random.seed(7)
b =np.random.randint(40,100,size=(5,6))
print(f'b={b}\nb中小于70的元素为:\n{b<70}')
ind = np.where(b<70,b,0)
print(f'np.where(b<70,b,0)=\n{ind}')

# 数组的运算和排序
a = np.arange(5)
a + 2
a * 3
a / 2 
a1 = np.tile(a , 4)
a2 = a1.reshape(4,-1)
a3 = np.arange(10,30).reshape(4,-1)
b = np.array([[1,2],[3,4]])
print(f'a3={a3}\na2={a2}\na3*a2={a3*a2}')

# 数组的排序
b = -np.sort(-a3)
print(b)


k = 0
while k < 4:
    print(np.random.randn(1,10))
    k += 1

a = np.arange(1,25)
b = np.random.choice(a,1)
print(b)