def read_file_and_answer(file_path):
    # mp for map because map is taken :(
    mp = []
    with open(file_path, 'r') as file:
        for line in file:
            mp.append(list(line.strip()))
    return small_cheat_count(mp)

def small_cheat_count(mp):
    n = len(mp)
    m = len(mp[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    START = 'S'
    END = 'E'
    OBSTACLE = '#'
    ans = 0

    si, sj = -1, -1
    ti, tj = -1, -1

    # find start and end cells
    for i in range(n):
        for j in range(m):
            if mp[i][j] == START: si, sj = i, j
            elif mp[i][j] == END: ti, tj = i, j
    
    # we will store the following, for each cell in the path:
    # the time to move from the start (si, sj) to this cell (i, j)
    reach_time = [[-1] * m for _ in range(n)]
    
    # compute the time to reach each cell on the path
    reach_time[si][sj] = 0
    i, j = si, sj
    while (i, j) != (ti, tj):
        for d in range(4):
            di, dj = dirs[d]
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if mp[ni][nj] != OBSTACLE and reach_time[ni][nj] == -1:
                    reach_time[ni][nj] = 1 + reach_time[i][j]
                    i, j = ni, nj
                    break 
    
    # store the total time to traverse the track
    total_time = reach_time[ti][tj]

    # compute the cheated time for each cell along the track
    cheat_dirs = [(2, 0), (-2, 0), (0, 2), (0, -2), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    i, j = si, sj
    while (i, j) != (ti, tj):
        for d in range(8):
            di, dj = cheat_dirs[d]
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and reach_time[ni][nj] != -1:
                # compute new time using the cheat
                # 2 picoseconds of time passed when the cheat is active
                # total_time - reach_time[ni][nj] is the time passed going from (ni, nj) to end cell
                new_time = reach_time[i][j] + 2 + (total_time - reach_time[ni][nj])
                if new_time <= total_time - 100:
                    ans += 1
        
        # move to the next cell on the path
        for d in range(4):
            di, dj = dirs[d]
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if mp[ni][nj] != OBSTACLE and reach_time[ni][nj] > reach_time[i][j]:
                    i, j = ni, nj
                    break

    return ans

    
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)