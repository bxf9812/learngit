import sys

# --------------------------------------------------------------------------------- #

def _reverse(graph):
    r = {}
    for src in graph:
        for (dst,c) in graph[src].items():
            if dst in r:
                r[dst][src] = c
            else:
                r[dst] = { src : c }
    return r

# Finds all cycles in graph using Tarjan's algorithm
def strongly_connected_components(graph):
    """
    Tarjan's Algorithm (named for its discoverer, Robert Tarjan) is a graph theory algorithm
    for finding the strongly connected components of a graph.

    Based on: http://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
    """

    index_counter = [0]
    stack = []
    lowlinks = {}
    index = {}
    result = []

    def strongconnect(node):
        # set the depth index for this node to the smallest unused index
        index[node] = index_counter[0]
        lowlinks[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)

        # Consider successors of `node`
        try:
            successors = graph[node]
        except:
            successors = []
        for successor in successors:
            if successor not in lowlinks:
                # Successor has not yet been visited; recurse on it
                strongconnect(successor)
                lowlinks[node] = min(lowlinks[node],lowlinks[successor])
            elif successor in stack:
                # the successor is in the stack and hence in the current strongly connected component (SCC)
                lowlinks[node] = min(lowlinks[node],index[successor])

        # If `node` is a root node, pop the stack and generate an SCC
        if lowlinks[node] == index[node]:
            connected_component = []

            while True:
                successor = stack.pop()
                connected_component.append(successor)
                if successor == node: break
            component = tuple(connected_component)
            # storing the result
            result.append(component)

    for node in graph:
        if node not in lowlinks:
            strongconnect(node)

    return result

def _mergeCycles(cycle,G,RG,g,rg):
    allInEdges = [] # all edges entering cycle from outside cycle
    minInternal = None
    minInternalWeight = sys.maxsize

    # Find minimal internal edge weight
    for n in cycle:
        for e in RG[n]:
            if e in cycle:
                if minInternal is None or RG[n][e] < minInternalWeight:
                    minInternal = (n,e)
                    minInternalWeight = RG[n][e]
                    continue
            else:
                allInEdges.append((n,e)) # edge enters cycle

    # Find the incoming edge with minimum modified cost
    # modified cost c(i,k) = c(i,j) - (c(x_j, j) - min{j}(c(x_j, j)))
    minExternal = None
    minModifiedWeight = 0
    for j,i in allInEdges: # j is vertex in cycle, i is candidate vertex outside cycle
        xj, weight_xj_j = rg[j].popitem() # xj is vertex in cycle that currently goes to j
        rg[j][xj] = weight_xj_j # put item back in dictionary
        w = RG[j][i] - (weight_xj_j - minInternalWeight) # c(i,k) = c(i,j) - (c(x_j, j) - min{j}(c(x_j, j)))
        if minExternal is None or w <= minModifiedWeight:
            minExternal = (j,i)
            minModifiedWeight = w

    w = RG[minExternal[0]][minExternal[1]] # weight of edge entering cycle
    xj,_ = rg[minExternal[0]].popitem() # xj is vertex in cycle that currently goes to j
    rem = (minExternal[0], xj) # edge to remove
    rg[minExternal[0]].clear() # popitem() should delete the one edge into j, but we ensure that

    # Remove offending edge from RG
    # RG[minExternal[0]].pop(xj, None) #highly experimental. throw away the offending edge, so we never get it again

    if rem[1] in g:
        if rem[0] in g[rem[1]]:
            del g[rem[1]][rem[0]]
    if minExternal[1] in g:
        g[minExternal[1]][minExternal[0]] = w
    else:
        g[minExternal[1]] = { minExternal[0] : w }

    rg = _reverse(g)

# --------------------------------------------------------------------------------- #

def mst(root,G):
    """ The Chu-Liu/Edmond's algorithm

    arguments:

    root - the root of the MST
    G - the graph in which the MST lies

    returns: a graph representation of the MST

    Graph representation is the same as the one found at:
    http://code.activestate.com/recipes/119466/

    Explanation is copied verbatim here:

    The input graph G is assumed to have the following
    representation: A vertex can be any object that can
    be used as an index into a dictionary.  G is a
    dictionary, indexed by vertices.  For any vertex v,
    G[v] is itself a dictionary, indexed by the neighbors
    of v.  For any edge v->w, G[v][w] is the length of
    the edge.
    """

    RG = _reverse(G)

    g = {}
    for n in RG:
        if len(RG[n]) == 0:
            continue
        minimum = sys.maxsize
        s,d = None,None

        for e in RG[n]:
            if RG[n][e] < minimum:
                minimum = RG[n][e]
                s,d = n,e

        if d in g:
            g[d][s] = RG[s][d]
        else:
            g[d] = { s : RG[s][d] }

    cycles = [list(c) for c in strongly_connected_components(g)]

    cycles_exist = True
    while cycles_exist:

        cycles_exist = False
        cycles = [list(c) for c in strongly_connected_components(g)]
        rg = _reverse(g)

        for cycle in cycles:

            if root in cycle:
                continue

            if len(cycle) == 1:
                continue

            _mergeCycles(cycle, G, RG, g, rg)
            cycles_exist = True

    return g

# --------------------------------------------------------------------------------- #

if __name__ == "__main__":

    # an example of an input that works
    root = 0
    g = {0: {1: 3}, 1: {2: 5, 5: 3}, 2: {4:1}, 3: {2: 5}, 4:{3:6, 5:2}, 5:{0:2, 2:3}}

    # an example of an input that causes infinite cycle
    # root = 0
    # g = {0: {1: 17, 2: 16, 3: 19, 4: 16, 5: 16, 6: 18}, 1: {2: 3, 3: 3, 4: 11, 5: 10, 6: 12}, 2: {1: 3, 3: 4, 4: 8, 5: 8, 6: 11}, 3: {1: 3, 2: 4, 4: 12, 5: 11, 6: 14}, 4: {1: 11, 2: 8, 3: 12, 5: 6, 6: 10}, 5: {1: 10, 2: 8, 3: 11, 4: 6, 6: 4}, 6: {1: 12, 2: 11, 3: 14, 4: 10, 5: 4}}

    h = mst(int(root),g)

    print(h)

    # for s in h:
    #     for t in h[s]:
    #         print ("%d-%d" % (s,t))