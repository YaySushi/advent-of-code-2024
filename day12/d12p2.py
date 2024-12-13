#pain.

def read_file_and_answer(file_path):
	# mp for map because map is taken :(
	mp = []
	with open(file_path, 'r') as file:
		for line in file:
			mp.append(list(line.strip()))
	return total_fencing_price(mp)

def total_fencing_price(mp):
	n = len(mp)
	m = len(mp[0])
	dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	price = 0
	perim = [[-1] * m for i in range(n)]

	def fence_cost(s, t):
		fence = mp[s][t]
		area = 0
		perimeter = 0

		mp[s][t] = mp[s][t].lower()
		stack = [(s, t)]

		while len(stack) > 0:
			(i, j) = stack.pop()

			# area contribution of current cell:
			area += 1

			# perimeter contribution of current cell
			# (could have been done in loop below but i like to seperate)
			sides = []
			oldp = perimeter
			for d in [0, 1, 2, 3]:
				(di, dj) = dirs[d]
				ni, nj = i + di, j + dj   # ni for new i, nj for new j
				if 0 <= ni < n and 0 <= nj < m and mp[ni][nj].lower() == fence.lower():
					sides.append(d)
			if len(sides) == 0: perimeter += 4
			elif len(sides) == 1: perimeter += 2	
			elif len(sides) == 2 and sum(sides) % 2 != 0: 
				#print((i, j))
				perimeter += 1
				[a, b] = sides
				if mp[i + dirs[a][0] + dirs[b][0]][j + dirs[a][1] + dirs[b][1]].lower() != fence.lower():
					perimeter += 1
			elif len(sides) == 3:
				[a, b, c] = sides
				if (a + b) % 2 == 0: # sides a and b are opposite.
					# check corner for a,c and b,c
					if mp[i + dirs[a][0] + dirs[c][0]][j + dirs[a][1] + dirs[c][1]].lower() != fence.lower():
						perimeter += 1
					if mp[i + dirs[b][0] + dirs[c][0]][j + dirs[b][1] + dirs[c][1]].lower() != fence.lower():
						perimeter += 1
				if (a + c) % 2 == 0: # sides a and c are opposite.
					if mp[i + dirs[b][0] + dirs[a][0]][j + dirs[b][1] + dirs[a][1]].lower() != fence.lower():
						perimeter += 1
					if mp[i + dirs[b][0] + dirs[c][0]][j + dirs[b][1] + dirs[c][1]].lower() != fence.lower():
						perimeter += 1
				if (b + c) % 2 == 0: # sides a and b are opposite.
					if mp[i + dirs[b][0] + dirs[a][0]][j + dirs[b][1] + dirs[a][1]].lower() != fence.lower():
						perimeter += 1
					if mp[i + dirs[c][0] + dirs[a][0]][j + dirs[c][1] + dirs[a][1]].lower() != fence.lower():
						perimeter += 1
			elif len(sides) == 4:
				if mp[i + dirs[0][0] + dirs[1][0]][j + dirs[0][1] + dirs[1][1]].lower() != fence.lower():
					perimeter += 1
				if mp[i + dirs[1][0] + dirs[2][0]][j + dirs[1][1] + dirs[2][1]].lower() != fence.lower():
					perimeter += 1
				if mp[i + dirs[2][0] + dirs[3][0]][j + dirs[2][1] + dirs[3][1]].lower() != fence.lower():
					perimeter += 1
				if mp[i + dirs[3][0] + dirs[0][0]][j + dirs[3][1] + dirs[0][1]].lower() != fence.lower():
					perimeter += 1
				
			perim[i][j] = perimeter - oldp
			for (di, dj) in dirs:
				ni, nj = i + di, j + dj   # ni for new i, nj for new j
				if 0 <= ni < n and 0 <= nj < m and mp[ni][nj] == fence: 
					mp[ni][nj] = fence.lower()
					stack.append((ni, nj))
		return area * perimeter

	for s in range(n):
		for t in range(m):
			if not mp[s][t].islower():
				price += fence_cost(s, t)

	return price

	
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)