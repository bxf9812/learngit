def make_mat(m, n, fill=None): # 初始化二维数组，生成空矩阵 (fill=元素=变量)
    mat = []
    for i in range(m): # 给i赋值m，默认从0开始，到m-1
        mat.append([fill] * n) # append=在列表末尾添加 在空矩阵中添加n个变量
    return mat # 选择性地返回一个值给调用方，不带表达式的return相当于返回None

INF = 1e6 # 初始化：数组全部赋值为INF（无穷大）

'''
dis[i][j]: 保存从顶点i到顶点j的已知最短路径, 初始化为直接连接
path[i][j]: 保存从顶点i到顶点j的已知最短路径上的下一个顶点, 初始化为j
'''

def show(dis, path):
    '''
    打印最短路径以及最短路权
    '''
    m = len(path)
    for i in range(m):
        for j in range(m):
            if i != j : 
                print("%d->%d: " % (i+1, j+1), end="")
                print(i+1, end=" ")
                k = path[i][j]
                while k != j: # 当k≠j时，证明有最短路经过k
                    print(k+1, end=" ")
                    k = path[k][j]  # 更新k
                print(j+1)
                print(dis[i][j]) # print各最短路的权


def floyd(graph):  # graph=邻接矩阵
    m = len(graph)  # m为邻接矩阵的行数（列表长度）
    dis = make_mat(m, m, fill=0)
    path = make_mat(m, m, fill=0)
    
    for i in range(m):
        for j in range(m):
            dis[i][j] = graph[i][j] # 初始化dis[i][j]为两点之间的权
            path[i][j] = j # 初始化path[i][j]为j
            if i == j : 
                dis[i][j] = 0  # 初始化各点到自己的距离为0

    for k in range(m):  # 最外层循环=从小到大枚举k
        for i in range(m):
            for j in range(m):
                if dis[i][k] + dis[k][j] < dis[i][j]: # if成立，找到中间节点k（找到第三个点代替使两点间的距离更短）
                    dis[i][j] = dis[i][k] + dis[k][j]
                    path[i][j] = path[i][k] # 初始化的最短路径上的下一个顶点j变成k，记录新路径的前驱
                
    return dis, path


if __name__ == '__main__':
    graph = make_mat(5, 5, fill=INF)
    graph[0][1] = 4
    graph[0][2] = 5
    graph[1][2] = 3
    graph[1][4] = 6
    graph[2][3] = -2
    graph[2][4] = 3
    graph[3][1] = 1
    graph[4][3] = 2
    graph[4][0] = -4

    dis, path = floyd(graph)
    show(dis, path)