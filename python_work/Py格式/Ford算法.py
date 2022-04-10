#!/usr/bin/env python
# coding: utf-8

# In[12]:


def bellman_ford(graph, source):
    dist = {}
    path = {}
    max = 10000
    for v in graph:
        dist[v] = max  #赋值为负无穷完成初始化
        path[v] = None
    dist[source] = 0
 
    for i in range(len( graph ) - 1):
        for u in graph:
            for v in graph[u]:
                if dist[v] > graph[u][v] + dist[u]:
                    dist[v] = graph[u][v] + dist[u]
                    path[v] = u    #完成松弛操作，p为前驱节点
 
    for u in graph:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                return None  #判断是否存在环路
 
    return dist, path
 
def test():
    graph = {
        'v1':{'v2': 1, 'v3': 5, 'v5':  3},
        'v2':{'v3':  2},
        'v3':{'v5':  -4},
        'v4':{ 'v3':  2},
        'v5':{'v4': 3}
    }
    dist, path = bellman_ford(graph, 'v1')
    print("从v1到各点的权重分别为：")    
    print(dist)    #从v1到v1,v2,v3,v4,v5的最短路的权重
    print("各点的前点分别为：")
    print(path)    ##从v1到v1,v2,v3,v4,v5的最短路的路径
test()

input("请按Enter键退出：")
# In[ ]:




