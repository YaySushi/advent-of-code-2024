def read_file_and_answer(file_path):
    # bytes was taken :(
    b8s = []
    with open(file_path, 'r') as file:
        for line in file:
            b8s.append(list(map(int, line.split(','))))
    return min_steps(b8s[:1024])

def min_steps(b8s):
    EMPTY = '.'
    FULL = '#'
    n = 71

    mp = [[EMPTY] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for [x, y] in b8s: mp[y][x] = FULL

    # an element of the queue is of the form (curr_x, curr_y, steps_so_far)
    qu = [(0, 0, 0)]

    while len(qu) > 0:
        x, y, s = qu.pop(0)

        if y == n - 1 and x == n - 1: return s

        if visited[y][x]: continue
        visited[y][x] = True

        for [dx, dy] in dirs:
            nx, ny = x + dx, y + dy  # nx for next x
            if 0 <= nx < n and 0 <= ny < n and mp[ny][nx] == EMPTY:
                qu.append((nx, ny, s + 1))
    
    return ':('

    
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)