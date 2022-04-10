# G 是临接表的方式表达图形
G={}
G[0] = {1,2}
G[1] = {0,1,3,4}
G[2] = {1,2}
G[3] = {1,2}
G[4] = {3,4}

match_list = [-1,-1,-1,-1,-1]

label_x = ['x1','x2','x3','x4','x5']
label_y = ['y1','y2','y3','y4','y5']

y_in_path = [False,False,False,False,False]

def find_agument_path(v):
    '''
    寻找增广路
    '''
    for i in G[v]:
        # 已经在交替路中出现的点就不需要匹配，避免死循环，例如 C 点需求增广路过程中，A 点不应该和E点再匹配
        if not y_in_path[i]: 
            y_in_path[i] = True
            if (match_list[i] == -1 or find_agument_path(match_list[i])):
                match_list[i] = v
                return True
    return False


def hungarian():

    for i in range(G.__len__()):
        global y_in_path
        # 清空交替路
        y_in_path = [False,False,False,False,False]
        find_agument_path(i)
    
    for i in range(match_list.__len__()):
        if match_list[i] == -1:continue
        print("%s <--match--> %s:" %(label_x[match_list[i]],label_y[i]))
        


if __name__ == "__main__":

    hungarian()