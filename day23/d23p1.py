def read_file_and_answer(file_path):
    conns = []
    with open(file_path, 'r') as file:
        for line in file:
            conns.append(line.strip().split('-'))
    return triplets(conns)

def triplets(conns):
    # create an adjacency list of all computers' neighbors
    nb = {}
    for [u, v] in conns:
       if u in nb: nb[u].append(v)
       else: nb[u] = [v]

       if v in nb: nb[v].append(u)
       else: nb[v] = [u]

    triplets = set()

    # manually look for three connected computers

    # u = comp 1
    for u in nb.keys():
        if not u.startswith('t'): continue
        # v = comp 2
        for v in nb[u]:
            # w = comp 3
            for w in nb[v]:
                if w != u and u in nb[w]:
                    # sort and add to a set to handle duplication
                    triplet = tuple(sorted([u, v, w]))
                    triplets.add(triplet)
    
    return len(triplets)

    
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)