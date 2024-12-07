def read_file_and_answer(file_path):
	# mp for map because map is taken :(
	mp = []
	with open(file_path, 'r') as file:
		for line in file:
			mp.append(line.strip())
	return guard_distinct_positions(mp)

def guard_distinct_positions(mp):
	n = len(mp)
	m = len(mp[0])
	dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	d = 0
	
	dir_i, dir_j = dirs[d]
	i, j = -1, -1
	visited = set()

	for a in range(n):
		for b in range(m):
			if mp[a][b] == '^': i, j = a, b

	visited.add((i, j))

	while 0 <= i + dir_i < n and 0 <= j + dir_j < m:
		if mp[i + dir_i][j + dir_j] == '#': d = (d + 1) % 4

		dir_i, dir_j = dirs[d]
		i, j = i + dir_i, j + dir_j
		visited.add((i, j))
	
	return len(visited)

	
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)