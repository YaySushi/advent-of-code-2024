def read_file_and_answer(file_path):
	# mp for map because map is taken :(
	mp = []
	with open(file_path, 'r') as file:
		for line in file:
			mp.append(list(line.strip()))
	return guard_loop_positions(mp)

def guard_loop_positions(mp):
	n = len(mp)
	m = len(mp[0])
	ans = 0
	for s in range(n):
		for t in range(m):
			if mp[s][t] == '^' or mp[s][t] == '#': continue
			else:
				mp[s][t] = '#'
				ans += check_for_loop(mp)
				mp[s][t] = '.'
	return ans

def check_for_loop(mp):
	n = len(mp)
	m = len(mp[0])
	dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	d = 0
	
	i, j = -1, -1
	visited = set()

	for a in range(n):
		for b in range(m):
			if mp[a][b] == '^': i, j = a, b
	
	# start at (i, j)
	visited.add((i, j, d))

	# next position:
	next_i, next_j = i + dirs[d][0], j + dirs[d][1]

	while 0 <= next_i < n and 0 <= next_j < m:
		if mp[next_i][next_j] == '#':  # if at obstacle, then go back and change dir
			next_i, next_j = next_i - dirs[d][0], next_j - dirs[d][1]
			d = (d + 1) % 4 
		if (next_i, next_j, d) in visited: return 1
		visited.add((next_i, next_j, d))
		next_i, next_j = next_i + dirs[d][0], next_j + dirs[d][1]
	
	return 0

	
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)