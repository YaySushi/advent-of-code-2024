def read_file_and_answer(file_path):
	# mp for map because map is taken :(
	mp = []
	with open(file_path, 'r') as file:
		for line in file:
			mp.append(list(map(int, line.strip())))
	return trailheads_score(mp)

def trailheads_score(mp):
	n = len(mp)
	m = len(mp[0])
	ans = 0

	for s in range(n):
		for t in range(m):
			if mp[s][t] == 0:
				ans += trailhead_score(mp, s, t)

	return ans

def trailhead_score(mp, s, t):
	n = len(mp)
	m = len(mp[0])
	dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	score = 0

	visited = set()

	stack = [(s, t)]

	while len(stack) > 0:
		(i, j) = stack.pop()
		visited.add((i, j))
		if mp[i][j] == 9: 
			score += 1
			continue
		for (di, dj) in dirs:
			ni, nj = i + di, j + dj   # ni for new i, nj for new j
			if 0 <= ni < n and 0 <= nj < m:
				if (ni, nj) in visited: continue
				if mp[i][j] + 1 != mp[ni][nj]: continue
				stack.append((ni, nj))
	
	return score

	
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)