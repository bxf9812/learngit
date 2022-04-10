INF = 1e6

def make_mat(m, n, fill=None):
    '''初始化二位数组'''
    mat = []
    for i in range(m):
        mat.append([fill] * n)
    return mat

def get_edges(graph):
    '''将图由邻接矩阵表示变换为边的列表'''
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    return edges

def ford(graph, v0):
    '''ford算法'''
    n = len(graph)
    edges = get_edges(graph)
    dis = [INF] * n
    dis[v0] = 0
    path = [0] * n
    for k in range(n-1):
        for edge in edges:
            # relax
            if dis[edge[0]] + edge[2] < dis[edge[1]]:
                dis[edge[1]] = dis[edge[0]] + edge[2]
                path[edge[1]] = edge[0]
    return dis, path

def show(path, start, stop):
    '''反向追踪法'''
    i = stop
    tmp = [stop]
    while i != start:
        i = path[i]
        tmp.append(i)
    return list(reversed(tmp))

if __name__ == '__main__':
    graph = make_mat(5, 5, fill=INF)
    graph[0][1] = -1
    graph[0][2] = 3
    graph[1][2] = 3
    graph[1][3] = 2
    graph[1][4] = 2
    graph[3][1] = 1
    graph[3][2] = 5
    graph[4][3] = -3

    dis, path = ford(graph, 0)

    v0 = 0
    for i in range(len(graph)):
        if i == v0:
            continue
        print("%d->%d: " % (v0, i), end="")
        print(show(path, v0, i))
        print(dis[i])

