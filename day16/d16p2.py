import heapq

def read_file_and_answer(file_path):
    # mp for map because map is taken :(
    mp = []
    with open(file_path, 'r') as file:
        for line in file:
            mp.append(list(line.strip()))
    return box_gps(mp)

def box_gps(mp):
    n = len(mp)
    m = len(mp[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    si, sj = -1, -1
    ti, tj = -1, -1

    for i in range(n):
        for j in range(m):
            if mp[i][j] == 'S': si, sj = i, j
            elif mp[i][j] == 'E': ti, tj = i, j
    
    # we will store the cheapest score to reach each coordinate ending in each 
    # possible direction. this is a 3d array
    scores = [[[float('inf')] * 4 for i in range(m)] for j in range(n)]
    # start east. lowest score is 0 by doing nothing
    scores[si][sj][1] = 0

    # initialize a priority queue with tuples of the form:
    # (starting row, starting col, index of distance in dirs array, score so far)
    pq = []
    heapq.heappush(pq, (0, si, sj, 1))

    while len(pq) > 0:
        s, i, j, d  = heapq.heappop(pq)

        if scores[i][j][d] < s: continue

        # keep going
        di, dj = dirs[d]
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and mp[ni][nj] != '#':
            ns = 1 + s
            if scores[ni][nj][d] > ns:
                scores[ni][nj][d] = ns
                heapq.heappush(pq, (ns, ni, nj, d))

        # turn one way
        d = (d + 1) % 4
        ns = 1000 + s
        if scores[i][j][d] > ns:
            scores[i][j][d] = ns
            heapq.heappush(pq, (ns, i, j, d))

        # turn the other way
        d = (d - 2) % 4
        ns = 1000 + s
        if scores[i][j][d] > ns:
            scores[i][j][d] = ns
            heapq.heappush(pq, (ns, i, j, d))

    # by now, we have the lowest score to go to each position on the map
    # walk backwards from the final position and check if we are along a
    # best path or not.

    qu = []
    visited = set({(i, j)})

    # fs: final score, fd: final direction
    fs = min(scores[ti][tj])
    for d in range(4):
        if scores[ti][tj][d] == fs:
            qu.append((ti, tj, d))
    
    # end position is a seat by default
    seats = 1

    while len(qu) > 0:
        i, j, d = qu.pop(0)

        # go backward
        di, dj = dirs[d]
        pi, pj = i - di, j - dj
        if 0 <= pi < n and 0 <= pj < m and mp[pi][pj] != '#':
            if scores[pi][pj][d] + 1 == scores[i][j][d] and (pi, pj) not in visited:
                visited.add((pi, pj))
                qu.append((pi, pj, d))
                seats += 1
        
        # turn
        # pd = previous direction
        pd = (d + 1) % 4
        if scores[i][j][pd] + 1000 == scores[i][j][d]:
            qu.append((i, j, pd))

        # turn
        pd = (d - 1) % 4
        if scores[i][j][pd] + 1000 == scores[i][j][d]:
            qu.append((i, j, pd))

    return seats

    
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)