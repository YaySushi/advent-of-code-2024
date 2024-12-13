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
			
			for (di, dj) in dirs:
				ni, nj = i + di, j + dj   # ni for new i, nj for new j
				if 0 <= ni < n and 0 <= nj < m:
					# perimeter contribution of current cell:
					if mp[ni][nj].lower() != fence.lower(): 
						perimeter += 1
						continue
					
					if mp[ni][nj] == fence: 
						mp[ni][nj] = fence.lower()
						stack.append((ni, nj))
				else:
					perimeter += 1
		return area * perimeter

	for s in range(n):
		for t in range(m):
			if not mp[s][t].islower():
				price += fence_cost(s, t)
	return price

	
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)