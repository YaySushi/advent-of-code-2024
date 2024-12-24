def read_file_and_answer(file_path):
    conns = []
    with open(file_path, 'r') as file:
        for line in file:
            conns.append(line.strip().split('-'))
    return password(conns)

def password(conns):
    # create an adjacency list of all computers' neighbors
    nb = {}
    for [u, v] in conns:
       if u in nb: nb[u].append(v)
       else: nb[u] = [v]

       if v in nb: nb[v].append(u)
       else: nb[v] = [u]

    cliks = []

    # start with cliques of size 1:
    cliks = [[u] for u in nb.keys()]
    
    while True:
        # keep new cliques as a tuple, so we can make it a set later to remove
        # duplicate cliques.
        new_cliks_tuple = []
        for clik in cliks:
            # check w can be added to make a bigger clique
            for w in nb.keys():
                # if w is already in the clique, do nothing
                if w in clik: continue

                # check if w has an edge to all nodes of clik:
                connected = True
                for u in clik:
                    if w not in nb[u]:
                        connected = False
                        break
                if connected:
                    # w can be added to make a bigger clique.

                    # make new clique a tuple that is sorted.
                    # makes sure that every arrangement of the nodes 
                    # ends up exactly the same (there is only one 
                    # alphabetical ordering of nodes)
                    new_clik_tuple = tuple(sorted(clik + [w]))
                    new_cliks_tuple.append(new_clik_tuple)
        
        # if no more clicks were generated, exit.
        if len(new_cliks_tuple) == 0: break

        cliks = [list(clik_tuple) for clik_tuple in set(new_cliks_tuple)]
    
    return ','.join(cliks[0])

    
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)