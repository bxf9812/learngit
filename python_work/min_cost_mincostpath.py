import numpy as np
import math
import Floyd
import copy

class edge:     #边类 纪录边的头 尾 容量c 权重w(cost),以及流量f
    def __init__(self, u, v, c,w):
        self.u = u
        self.v = v
        self.c = c
        self.w = w
        self.f = 0

def matrix(edges,n,m):
    wmat=np.full((n,n),math.inf) #开局先赋为最大值

    for i in range(n):
        wmat[i][i]=0

    for i in range(m):
        wmat[edges[i].u][edges[i].v]=edges[i].w

    return wmat

def mincost(edges, n, m, f0):  #f0为固定流量,若f0 = inf 则求最小费用最大流
    edges_c = copy.deepcopy(edges)
    f = 0
    while(1):
        u = copy.deepcopy((matrix(edges_c,n ,m)))  # 记录两点之间最短路径的u矩阵，初始化为权值矩阵
        r = np.full((n, n), 0)  # 记录两点间最短路径的第一条弧的头，从起点向前检索可以得到完整的最短路
        u ,r ,ans= Floyd.floyd(matrix(edges_c,n ,m), n, m) #使用Floyd算法计算从Vs到Vt的最短路
        path = []
        path.append(0)
        if u[0][n-1] != math.inf:
            head = r[0][n-1]  # 更新要找的弧的头
            path.append(head)
            while head != n-1:  # 直到我们找到了目标路径的终点
                head = r[head][n-1]
                path.append(head)
        elif f0 == math.inf :
            print("最大流量为{}".format(f))
            return edges
        else :
            print("no answer")
            return False
        #print(path)
        length = len(path) - 1
        c0 = math.inf #为本次新增的流量
        path_i = [] #增广链的边序号
        for i in range(length):
            for j in range(m):
                if edges[j].u == path[i] and edges[j].v == path[i+1]: #遍历增广链中的边,得到所需要增加的流量c0
                    path_i.append(j)
                    c = edges[j].c - edges[j].f
                    if c < c0 :
                        c0 = c
        if f + c0 < f0:
            f = f + c0
            for i in path_i:
                edges[i].f += c0
                if edges[i].f == edges[i].c:
                    edges_c[i].w = math.inf   #如果该边中流量等于容量,说明其不可通
        else:
            c0 = f0 - f
            for i in path_i:
                    edges[i].f += c0   #已经得到答案
            return edges


if __name__ == '__main__':
    n = 5
    m = 7
    edges = []
    u, v, c, w = [1, 2, 3, 2]
    edges.append(edge(u - 1, v - 1, c, w))
    u, v, c, w = [1, 4, 2, 3]
    edges.append(edge(u - 1, v - 1, c, w))
    u, v, c, w = [2, 3, 3, 4]
    edges.append(edge(u - 1, v - 1, c, w))
    u, v, c, w = [2, 4, 1, 1]
    edges.append(edge(u - 1, v - 1, c, w))
    u, v, c, w = [4, 3, 2, 5]
    edges.append(edge(u - 1, v - 1, c, w))
    u, v, c, w = [3, 5, 3, 1]
    edges.append(edge(u - 1, v - 1, c, w))
    u, v, c, w = [4, 5, 3, 2]
    edges.append(edge(u - 1, v - 1, c, w))
    edges = mincost(edges, n, m, 4)
    for i in range(m):
        if edges[i].f > 0:
            print(edges[i].u, edges[i].v, edges[i].f)


