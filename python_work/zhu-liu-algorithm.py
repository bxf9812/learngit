class Edge: # 表示从u指向v的权值为w的有向边

    def __init__(self, u, v, w): # 有参构造函数，实例化时直接传入参数

        self.u = u

        self.v = v

        self.w = w


    def __str__(self):

        return str(self.u) + str(self.v) + str(self.w)



def zhuliu(edges, n, m, root):  # n个点，m条边，root根节点

    res = 0  # 统计边权的和

    while True:

        pre = [-1]*n  # 存储前驱顶点

        visited = [-1] * n  # 访问标记

        circle = []  # 记录节点i所在环的编号

        inderee = [INF] * n  # 记录i入边中最小权值

        # 寻找最小入边

        inderee[root] = 0

        for i in range(m):

            if edges[i].u != edges[i].v and edges[i].w < inderee[edges[i].v]: # 忽略自环

                pre[edges[i].v] = edges[i].u

                inderee[edges[i].v] = edges[i].w  # 对于每个点选择权值最小的入边,用inderee记录

        # 有孤立点，不存在最小树形图

        for i in range(n):

            if i != root and inderee[i] == INF: # if i入边中最小权值为∞

                return -1

        # 找有向环

        tn = 0  # 记录环的个数

        circle = [-1] * n

        for i in range(n):

            res += inderee[i] # 累加

            v = i

            '''
            向前遍历找环，中止情况有：

            1. 出现带有相同标记的点，成环

            2. 节点属于其他环，说明进了其他环

            3. 遍历到root了
            '''

            while visited[v] != i and circle[v] == -1 and v != root:

                visited[v] = i  # 如果有环，visited[v] = i时会退出回到起点

                v = pre[v]  # 迭代前驱顶点直到更新到根

            '''
            如果成环了才会进下面的循环，把环内的点的circle进行标记
            '''

            if v != root and circle[v] == -1: # 在环上（不是以root为根节点）且环没被处理过

                while circle[v] != tn:

                    circle[v] = tn # 记录节点所属的环的编号

                    v = pre[v]

                tn += 1  # 环编号累加

        # 如果没有环了，说明一定已经找到了

        if tn == 0:

            break  # 不存在有向环

        # 否则把孤立点都看作自环看待

        for i in range(n):

            if circle[i] == -1:

                circle[i] = tn

                tn += 1 # 环数累加

        # 进行缩点，把点号用环号替代

        for i in range(m):

            v = edges[i].v

            edges[i].u = circle[edges[i].u]

            edges[i].v = circle[edges[i].v]  # u到v是一个有向边

            # 如果两点不属于同一个环,更新边权,u到v的距离=边权-inderee[v]

            if edges[i].u != edges[i].v:

                edges[i].w -= inderee[v]

        n = tn # 用环的数量作为下一轮迭代的点数，继续执行至无环

        root = circle[root] # 更新根节点的编号

    return res



INF = 9999999999

if __name__ == '__main__':

    f = open('testData.txt')

    n, m, root = list(map(int, f.readline().split()))

    #n, m, root = list(map(int, input().split()))

    edges = []

    for i in range(m):

        u, v, w = list(map(int, f.readline().split()))

        # 输入的点是1开始的，-1改为0开始的

        edges.append(Edge(u-1, v-1, w))

    print(zhuliu(edges, n, m, root-1),end = "")