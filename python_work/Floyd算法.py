
def make_mat(m, n, fill=None):
    mat = []
    for i in range(m):
        mat.append([fill] * n)
    return mat

INF = 1e6


def show(dis, path):
    m = len(path)
    for i in range(m):
        for j in range(i + 1, m):
            print("%d->%d: " % (i+1, j+1), end=" ")
            k = path[i][j]
            print(i+1, end=" ")
            while k != j:
                print(k+1, end=" ")
                k = path[k][j]

            print(j+1)
            print(dis[i][j])


def floyd(graph):
    m = len(graph)

    dis = make_mat(m, m, fill=0)
    path = make_mat(m, m, fill=0)
    for i in range(m):
        for j in range(m):
            dis[i][j] = graph[i][j]
            path[i][j] = j

    for k in range(m):
        for i in range(m):
            for j in range(m):
                if dis[i][k] + dis[k][j] < dis[i][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
                    path[i][j] = path[i][k]

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
