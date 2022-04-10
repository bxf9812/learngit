inf = 99999
import copy

# 定义函数，计算剩余网络 p118
def cal_res_net(D, f):
    n = len(D)
    res_net = [[inf for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if D[i][j] != inf and D[i][j] - f[i][j] > 0:
                res_net[i][j] = D[i][j] - f[i][j]  # 正向弧：容量-流量
            if D[i][j] != inf and f[i][j] > 0:
                res_net[j][i] = f[i][j]  # 反向弧：流量
    return res_net


# 定义函数，计算分层剩余网络AD
def cal_AD(res_net, s, t):
    n = len(res_net)  #
    nodes = set(range(n))
    current_nodes = set([s])  # 标记但没有检查的点
    res_nodes = nodes - current_nodes  # 没有标记且没有检查的点
    AD = [[inf for i in range(n)] for j in range(n)]  # 初始化AD内各元素为inf
    while True:
        temp = []  # 存储下一轮标记但没有检查的点
        for i in current_nodes:
            for j in res_nodes:
                if res_net[i][j] != inf:
                    AD[i][j] = res_net[i][j]
                    temp.append(j)
        temp = set(temp)
        if res_nodes == res_nodes - temp:
            if t in res_nodes:
                print('计算得到的分层剩余网络无法继续增广')
                return -1
            return AD  # 如果t已经检查，说明分层剩余网络中还存在（s,t）路,

        current_nodes = temp
        res_nodes = res_nodes - temp



# 在分层剩余网络中找一条（s,t）路
def find_path(AD, s, t):
    path = [s]
    n = len(AD)
    v = s  # v:当前访问到的点
    nodes_r = [i for i in range(n) if i != s]
    while True:
        iter_num = 0
        max_iter = len(nodes_r)
        for k in nodes_r:
            if AD[v][k] != inf:
                path.append(k)
                nodes_r.remove(k)
                if k == t:
                    return path  # 找到（s,t）路
                v = k
                break
            else:
                iter_num += 1
        if iter_num != max_iter:
            continue

        if v == s:
            # print('不存在（s,t）路')
            return -1
        path.remove(v)  # 找不到v的出邻点，回退
        v = path[-1]


# 计算路径最大容量
def get_flow(AD, path):
    max_flow = AD[path[0]][path[1]]
    for i in range(len(path) - 1):
        if AD[path[i]][path[i + 1]] < max_flow:
            max_flow = AD[path[i]][path[i + 1]]

    return max_flow


# 定义函数，最短增广链算法,增广流值到指定值
def aug_flow(D, f, s, t, v0):
    current_flow = 0  # 当前的流值
    # while current_flow!=v0:
    res_net = cal_res_net(D, f)
    AD = cal_AD(res_net, s, t)
    while AD != -1: # 根据剩余网络计算出的分层剩余网络无法增广
        path = find_path(AD, s, t)
        while path != -1: # 没找到（s,t）路
            add_flow_max = get_flow(AD, path)
            # if current_flow==v0:                                    #流值已经达到v0,返回f；否则继续增流
            # return f
            '''
            流值需达到v0
            current_flow 当前可行流流值
            add_flow_max 增广路能够增广的最大流值
            '''
            if current_flow + add_flow_max < v0:  # 如果<v0，增广找到的增广路径的全部流值
                for i in range(len(path) - 1):
                    f[path[i]][path[i + 1]] += add_flow_max
                    AD[path[i]][path[i + 1]] -= add_flow_max
                    if AD[path[i]][path[i + 1]] == 0:
                        AD[path[i]][path[i + 1]] = inf
                current_flow += add_flow_max
            else:  # 增加增广路的部分（需要的）流值，使流值达到v0
                need_flow = v0 - current_flow
                for i in range(len(path) - 1):
                    f[path[i]][path[i + 1]] += need_flow
                    AD[path[i]][path[i + 1]] -= need_flow
                return f

            path = find_path(AD, s, t)
        res_net = cal_res_net(D, f)
        AD = cal_AD(res_net, s, t)
    print('不存在流值为{}的可行流'.format(v0))
    return -1


# aug_flow(D,f,0,5,4)
# 使用ford算法找负回路
def ford(w, start_node):
    '''
    输入：有向图的邻接矩阵和起始顶点标号
    输出：起始节点到其他每个节点最短路的权重u和前点标号集l
    '''
    n = len(w[0])
    l = [start_node] * n
    l[start_node] = -1
    u = w[start_node][:]  # 初始化各最短路权重
    k = 0
    while k != n - 1:
        for i in range(n):
            for j in range(n):
                if u[i] > u[j] + w[j][i] and u[j] != inf and w[j][i] != inf:  # 根据P90定理5.7更新u和l
                    u[i] = u[j] + w[j][i]
                    l[i] = j
        k += 1

    u_n = u[:]  # 负回路判别过程。进行第n次权重更新得到u_n
    for i in range(n):
        for j in range(n):
            if u[i] > u[j] + w[j][i] and u[j] != inf and w[j][i] != inf:
                u_n[i] = u[j] + w[j][i]
                l[i] = j
    neg_circle = []  # circle储存负回路
    k = 0
    for i in range(n):
        if u_n[i] != u[i]:
            current_node = i
            neg_circle.insert(0, current_node)
            current_node = l[i]
            while current_node != i:  # 计算负回路
                neg_circle.insert(0, current_node)
                current_node = l[current_node]
            neg_circle.insert(0, current_node)
            # print("存在负回路：",neg_circle)
            return neg_circle  # 输出负回路
    u = u_n  # 如果不存在负回路，返回-1
    # print('不存在负回路')
    return -1

# 计算剩余网络的费用网络
def cal_cost_res(res_net, cost_net):
    cost_res_net = copy.deepcopy(res_net)
    n = len(res_net)
    for i in range(n):
        for j in range(n):
            if res_net[i][j] != inf:
                if cost_net[i][j] != inf:
                    cost_res_net[i][j] = cost_net[i][j]
                else:
                    cost_res_net[i][j] = -cost_net[j][i] # 反向弧 费用变为相反数
    return cost_res_net


# 最小费用流算法
def min_cost_flow(D, cost_net, s, t, v0): # 容量网络，费用网络，发点，收点，可行流 v0=4 求流值为4的最小费用流
    n = len(D)
    f = copy.deepcopy(D)
    for i in range(n):
        for j in range(n):
            if D[i][j] != inf:
                f[i][j] = 0  # 初始化流值为0流
    f = aug_flow(D, f, s, t, v0)  # 最大流算法增广到将流值增广到v0
    if f == -1:
        return -1
    while True:
        # print('f: ',f)
        res_net = cal_res_net(D, f)
        # print('res_net: ',res_net)
        cost_res = cal_cost_res(res_net, cost_net)
        # print('cost_res: ',cost_res)
        cost_copy = copy.deepcopy(cost_res)
        for i in range(n):
            cost_copy[i][i] = 0
        # while True:
        neg_circle = ford(cost_copy, s)  # 使用ford算法找费用负回路
        # print('neg_circle:',neg_circle)
        if neg_circle == -1:
            return f

        add_flow = get_flow(res_net, neg_circle)  # 负回路能增广的最大流值
        # print('add_flow:',add_flow)
        for i in range(len(neg_circle) - 1):
            if cost_res[neg_circle[i]][neg_circle[i + 1]] > 0:
                f[neg_circle[i]][neg_circle[i + 1]] += add_flow # 正向弧＋扩充量
            else:
                f[neg_circle[i + 1]][neg_circle[i]] -= add_flow # 反向弧-扩充量

# 获取可行流的最小费用
def get_path_cost(f, cost_net):
    cost = 0
    path = []
    n = len(f)
    for i in range(n):
        for j in range(n):
            if f[i][j] != inf:
                path.append([i, j])
                cost += cost_net[i][j]*f[i][j]
    return path, cost


if __name__ == '__main__' :
    # 邻接矩阵 例题P134
    D = [[inf, 3, inf, 2, inf],
        [inf, inf, 3, 1, inf],
        [inf, inf, inf, inf, 3],
        [inf, inf, 2, inf, 3],
        [inf, inf, inf, inf, inf]]
    cost_net = [[inf, 2, inf, 3, inf], 
                [inf, inf, 4, 1, inf], 
                [inf, inf, inf, inf, 1], 
                [inf, inf, 5, inf, 2],
                [inf, inf, inf, inf, inf]]

    f = min_cost_flow(D, cost_net, 0, 4, 4) # v0=4 求流值为4的最小费用流
    path, cost = get_path_cost(f, cost_net)
    print('path: ', path, '\ncost: ', cost)
