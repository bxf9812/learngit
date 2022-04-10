'''
姓名： 方雨晔
学号： 20214507021
班级:  应用统计
'''
import numpy as np
import math

class edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
#权值矩阵的初始化 即U0
def matrix(edges,n,m):
    wmat=np.full((n,n),math.inf) #开局先赋为最大值

    for i in range(n):
        wmat[i][i]=0

    for i in range(m):
        wmat[edges[i].u][edges[i].v]=edges[i].w

    return wmat

def floyd(wmat,n,m):

    u=wmat    #记录两点之间最短路径的u矩阵，初始化为权值矩阵
    r=np.full((n,n),0)    #记录两点间最短路径的第一条弧的头，从起点向前检索可以得到完整的最短路
    # R0
    for i in range(n):
        for j in range(n):
            r[i][j]=j
    k=0

    while k < n:
        '''
        应用P94公式
        '''
        for i in range(n):
            for j in range(n):
                if u[i][j] > u[i][k]+u[k][j]:
                    u[i][j]=u[i][k]+u[k][j]
                    r[i][j]=r[i][k]
        k+=1

    #负回路检测
    for i in range(n):
        if u[i][i] < 0:
            print('网络中包含负回路!')
            return u,r

    #输出最短路径
    ans = np.full((n,n),None) #初始化
    for i in range(n):
        for j in range(n):
            if i != j and u[i][j] != math.inf:
                path = 'v{}'.format(i+1)  #path为记载最短路径
                head=r[i][j]  #更新要找的弧的头
                while head != j:  #直到我们找到了目标路径的终点
                    path += 'v{}'.format(head+1)
                    head=r[head][j]
                path += 'v{}'.format(j+1) #最后把终点放入
                ans[i][j]=path
            else:
                ans[i][j] = ''

    return u,r,ans

if __name__ == '__main__':
    print("例1:")
    n=5
    m=9
    edges = []
    u, v, w = [1, 2, 4]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [1, 3, 5]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [2, 3, 3]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [2, 5, 6]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [3, 4, -2]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [3, 5, 3]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [4, 2, 1]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [5, 1, -4]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [5, 4, 2]
    edges.append(edge(u - 1, v - 1, w))

    wmat=matrix(edges,n,m)
    u,r,ans=floyd(wmat, n, m)

    print(u)
    print(r+np.full((n,n),1))
    print(ans)

    print("例2:")
    n=5
    m=8
    edges = []
    u, v, w = [1, 2, 1]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [2, 3, 5]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [2, 5, -3]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [3, 5, 2]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [4, 1, 3]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [4, 3, 6]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [5, 1, 4]
    edges.append(edge(u - 1, v - 1, w))
    u, v, w = [5, 4, -2]
    edges.append(edge(u - 1, v - 1, w))

    wmat=matrix(edges,n,m)
    u, r =floyd(wmat, n, m)
    print(u)
    print(r + np.full((n, n), 1))



