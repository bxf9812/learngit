import queue


def expand(G, G_prime, P_prime):

    if not len(G) in P_prime:
        return P_prime
    else:
        cycle = G_prime[-1]['cycle']
        position = P_prime.index(len(G))
        if position % 2 == 0:
            reverse_middle = True
            non_stem_neighbor = P_prime[position + 1]
        else:
            reverse_middle = False
            non_stem_neighbor = P_prime[position - 1]

        if cycle[0] in G[non_stem_neighbor]['adj']:
            P_prime[position] = cycle[0]
            return P_prime

        else:
            first_half = P_prime[:position]
            second_half = P_prime[position + 1:]
            for i in range(len(cycle)):
                if non_stem_neighbor in G[cycle[i]]['adj']:
                    start = i
                    break

            middle = []
            if G[cycle[start]]['partner'] == cycle[start - 1]:
                for i in range(start, -1, -1):
                    middle.append(cycle[i])
            else:
                for i in range(start, len(cycle)):
                    middle.append(cycle[i])

            P = first_half
            if reverse_middle:
                middle.reverse()
            P = P + middle
            P = P + second_half
            return P
    return []



def contract(G, v, w):
    path_to_stem_v = [v]
    path_to_stem_w = [w]
    while G[v]['parent'] != -1:
        path_to_stem_v.append(G[v]['parent'])
        v = G[v]['parent']
    while G[w]['parent'] != -1:
        path_to_stem_w.append(G[w]['parent'])
        w = G[w]['parent']
    while len(path_to_stem_v) > 0 and len(path_to_stem_w) > 0:
        if path_to_stem_v[-1] == path_to_stem_w[-1]:
            lowest_common_ancestor = path_to_stem_v[-1]
            path_to_stem_v = path_to_stem_v[:-1]
            path_to_stem_w = path_to_stem_w[:-1]
        else:
            break


    cycle = [lowest_common_ancestor]
    for i in reversed(path_to_stem_w):
        cycle.append(i)
    cycle = cycle + path_to_stem_v + [lowest_common_ancestor]
    blossom_verteces = set(cycle)

    blossom_vertex = {'adj': [], 'partner': -1, 'blossom': -1, 'cycle': cycle}

    contracted_G = []
    for i in range(len(G)):
        vertex = {}
        if G[i]['blossom'] != -1:
            vertex['blossom'] = G[i]['blossom']
        else:
            if i in blossom_verteces:
                vertex['blossom'] = len(G)
            else:
                vertex['blossom'] = -1
                if G[i]['partner'] in blossom_verteces:
                    vertex['partner'] = len(G)
                    blossom_vertex['partner'] = i
                else:
                    vertex['partner'] = G[i]['partner']


                vertex['adj'] = []
                adjacent_to_blossom = False
                for j in G[i]['adj']:
                    if j in blossom_verteces:
                        adjacent_to_blossom = True
                    else:
                        vertex['adj'].append(j)
                if adjacent_to_blossom:
                    vertex['adj'].append(len(G))
                    blossom_vertex['adj'].append(i)

        contracted_G.append(vertex)
    contracted_G.append(blossom_vertex)
    return contracted_G


def max_matching(adj):
    def invert(aug_path, G):
        for i in range(len(aug_path) // 2):
            G[aug_path[2 * i]]['partner'] = aug_path[2 * i + 1]
            G[aug_path[2 * i + 1]]['partner'] = aug_path[2 * i]

    def find_aug_path(G):
        def add_match_to_tree(v, w, w_partner):
            G[w]['parent'] = v
            G[w_partner]['parent'] = w
            G[w]['root'] = G[v]['root']
            G[w_partner]['root'] = G[v]['root']
            G[w]['distance'] = G[v]['distance'] + 1
            G[w_partner]['distance'] = G[v]['distance'] + 2


        forest = []
        for i in range(len(G)):
            if G[i]['blossom'] == -1:
                G[i]['parent'] = -1
                if G[i]['partner'] == -1:
                    forest.append(i)
                    G[i]['distance'] = 0
                    G[i]['root'] = i
                else:
                    G[i]['distance'] = len(G) + 1
                    G[i]['root'] = -1
        for i in forest:
            q = queue.Queue()
            q.put(i)
            while not q.empty():
                v = q.get()

                for w in G[v]['adj']:
                    if G[w]['partner'] == -1:
                        P = [v, w]
                        while (G[v]['parent'] != -1):
                            P.insert(0, G[v]['parent'])
                            v = G[v]['parent']
                        while (G[w]['parent'] != -1):
                            P.append(G[w]['parent'])
                            w = G[w]['parent']
                        return P
                for w in G[v]['adj']:
                    if G[w]['partner'] != -1 and G[w]['root'] == -1:
                        add_match_to_tree(v, w, G[w]['partner'])
                        q.put(G[w]['partner'])
                    elif G[w]['distance'] % 2 == 1:
                        pass
                    elif G[w]['distance'] % 2 == 0 and G[w]['root'] == G[v]['root']:
                        G_prime = contract(G, v, w)
                        P_prime = find_aug_path(G_prime)
                        P = expand(G, G_prime, P_prime)
                        return P
                    else:
                        P = [v, w]
                        while G[v]['parent'] != -1:
                            P.insert(0, G[v]['parent'])
                            v = G[v]['parent']
                        while G[w]['parent'] != -1:
                            P.append(G[w]['parent'])
                            w = G[w]['parent']
                        return P
        return []


    G = []
    for i in range(len(adj)):
        vertex = {
            'partner': -1,
            'blossom': -1,
            'adj': []}
        for j in adj[i]:
            vertex['adj'].append(j)
        G.append(vertex)

    while True:
        aug_path = find_aug_path(G)
        if len(aug_path) == 0:
            break
        else:
            invert(aug_path, G)

    matching = [];
    for i in range(len(G)):
        if i < G[i]['partner']:
            matching.append((i, G[i]['partner']))
    return matching

