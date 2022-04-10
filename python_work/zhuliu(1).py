def msa(V, E, r, w):
    """
    V是点的集合
    E是边的集合，用（u,v）表示
    r是根节点
    w是dict( Edge(u,v) : cost)
    """

    """
    Step 1 : 删除根节点的入弧   
    """
    for (u, v) in E.copy():
        if v == r:
            E.remove((u, v))
            w.pop((u, v))

    """
    Step 2 : 找出每个点的最小入弧。
    """
    pre = dict()
    for v in V:
        edges = [edge[0] for edge in E if edge[1] == v] #找出所有头是v的弧，列表中是这些弧的尾
        if len(edges) == 0:
            continue
        costs = [w[(u, v)] for u in edges]
        pre[v] = edges[costs.index(min(costs))] #是一个字典，键为v，值为u

    if len(pre) < len(V) -1:
        return None


    """
    Step 3 : 在图中找圈
    """
    cycle_vertex = None
    for v in V:
        if cycle_vertex is not None:
            break
        visited = set()
        pre_v = pre.get(v)
        while pre_v:
            if pre_v in visited:
                cycle_vertex = pre_v
                break
            visited.add(pre_v)
            pre_v = pre.get(pre_v)
#对每一个点，建立一个空集合，得到它的上一个点,当上一个点存在时，判断是否标记过，若标记过则有圈
    """
    Step 4 :如果没有圈,返回所有的最小入弧
    """
    if cycle_vertex is None:
        return set([(pre[v], v) for v in pre.keys()])

    """
    Step 5 : 将圈里的点都做标记
    """
    circle = set()
    circle.add(cycle_vertex)
    pre_v = pre.get(cycle_vertex)
    while pre_v != cycle_vertex:
        circle.add(pre_v)
        pre_v = pre.get(pre_v)

    """
    Step 6 : 缩点，点号进行平方取相反数  先建立新的点，边，权重集
    """
    v_c = -cycle_vertex ** 2
    V_prime = set([v for v in V if v not in circle] + [v_c])
    E_prime = set()
    w_prime = dict()
    correspondance = dict()
    for (u, v) in E:
        if u not in circle and v in circle:
            e = (u, v_c)
            if e in E_prime:
                if w_prime[e] < w[(u,v)] - w[(pre[v],v)]:
                    continue
            w_prime[e] = w[(u,v)] - w[(pre[v],v)]
            correspondance[e] = (u,v)
            E_prime.add(e)
        elif u in circle and v not in circle:
            e = (v_c, v)
            if e in E_prime:
                old_u = correspondance[e][0]
                if w[(old_u, v)] < w[(u, v)]: #找权重最小的
                    continue
            E_prime.add(e)
            w_prime[e] = w[(u, v)]
            correspondance[e] = (u, v)
        elif u not in circle and v not in circle:
            e = (u, v)
            E_prime.add(e)
            w_prime[e] = w[(u, v)]
            correspondance[e] = (u, v)

    """
    Step 7 : 递归算法直到图中没有圈
    """

    tree = msa(V_prime, E_prime, r, w_prime)

    cycle_edge = None
    for (u, v) in tree:
        if v == v_c:
            old_v = correspondance[(u, v_c)][1] #对每一个进入圈的弧，得到原来的头
            cycle_edge = (pre[old_v], old_v)#圈里以该顶点为头的弧
            break

    ret = set([correspondance[(u, v)] for (u, v) in tree]) #树里面每一条弧原来的头和尾
    for v in circle:
        u = pre[v]
        ret.add((u, v))

    ret.remove(cycle_edge)

    return ret

if __name__ == '__main__':
    V = set([1,2,3,4,5,6])
    E = set([(1,2),(6,1),(2,6),(2,3),(6,3),(5,6),(3,5),(4,3),(5,4)])
    r = 4
    w = {(1,2):3,(6,1):2,(2,3):5,(2,6):3,(6,3):3,(5,6):2,(3,5):1,(4,3):5,(5,4):6}
    msa(V,E,r,w)
    print(V , E)

