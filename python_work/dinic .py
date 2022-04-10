from queue import Queue

#n #边的个数
m = 6#点的个数

residual = [[0 for i in range(m)] for j in range(m)]
#残余图的剩余流量
maxflowgraph = [[0 for i in range(m)] for j in range(m)]
#记录最大流图，初始都为0
flow = [0 for i in range(m)]
#记录增广路径前进过程记录的最小流量
pre = [float('inf') for i in range(m)]
#记录增广路径每个节点的前驱，也记录该节点是否被路径记录

level = [float('inf') for i in range(m)]
#代表层次图，层次从0开始

sumflow = 0

#设置初始图的流量走向
residual[0][1]=4
residual[0][3]=6
residual[1][2]=2
residual[1][3]=2
residual[1][4]=1
residual[2][5]=4
residual[4][2]=3
residual[3][4]=5
residual[4][5]=7

def build_level(source,sink):
    #根据残余图来构建层次图,过程类似无权最短路径
    level[source] = 0#源点的层次为0
    level_pre = [float('inf') for i in range(m)]
    #构造层次图用到的前驱表，用来标记该节点已标记为层次
    q = Queue()
    #队列，用于BFS地寻找增广路径
    q.put(source)
    while(not q.empty()):
        current = q.get()
        for i in range(m):
            if( (i==source) | (i==current) ):
                continue#源点和自身不用分析
            if((residual[current][i]>0)&(level_pre[i]==float('inf'))):
                #只要能往下走且没有被标记过
                level_pre[i] = current
                #标记前驱，也代表已构造了层次
                level[i] = level[current]+1
                #层次逐渐加1
                q.put(i)
                #加入队列
    print('层次图为',level)
    if(level_pre[sink]!=float('inf')):
        #如果构造层次图能构造到sink点，说明有增广路径
        return True
    else:
        return False

def get_augment(source,sink):
    #根据层次图，构造可能的增广路径
    temp_augment = [source]
    #每条增广路径都是从源点开始的
    count = 1#源点下一层的层次为1
    def recursion(count):
        for i in range(m):
            if(level[i]==count):#寻找层次为count的点
                temp_augment.append(i)
                if(i == sink):
                    #i到了sink，说明找到了一条可能的增广路径
                    print('可能的增广路径',temp_augment)
                    #可能的增广路径是层次图的排列组合而来
                    send_flow(temp_augment,source,sink)
                recursion(count+1)#寻找下一层次的点
                temp_augment.remove(i)
                #删除掉i，为下一次递归作准备
    recursion(count)
    print()

def send_flow(augment,source,sink):
    #根据可能的增广路径，判断其是否为一条可行的增广路径
    global sumflow

    flow[sink] = float('inf')#设为无穷，且以这个作为找到增广路径的标志
    print('初始flow',flow)
    for i in range(len(augment)-1):
        flow[augment[i+1]] = min(flow[augment[i]],residual[augment[i]][augment[i+1]])
        print('行进增广路径过程中的flow',flow)
    if(flow[sink] != 0):
        #flow[sink]不为0，说明增广路径有效
        sumflow += flow[sink]
        print('有效的增广路径',augment,flow)
        for i in range(len(augment)-1):
            #对残余图和最大流图的相应修改
            residual[augment[i]][augment[i+1]] -= flow[sink]
            residual[augment[i+1]][augment[i]] += flow[sink]
            maxflowgraph[augment[i]][augment[i+1]] += flow[sink]  
    print()

def dinic(source,sink):
    flow[source] = float('inf')
    #源点的flow为无穷，方便以后取较小数，且源点的flow永远为无穷
    while(True):
        temp = build_level(source,sink)
        if(temp is False):
            break
        else:
            get_augment(source,sink)

dinic(0,m-1)
print(sumflow)
print(maxflowgraph)