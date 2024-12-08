from collections import defaultdict

def read_file_and_answer(file_path):
	# mp for map because map is taken :(
	mp = []
	with open(file_path, 'r') as file:
		for line in file:
			mp.append(line.strip())
	return antinode_count(mp)

def antinode_count(mp):
	n = len(mp)
	m = len(mp[0])

	antennas = defaultdict(list)
	antinodes = set()


	for i in range(n):
		for j in range(m):
			if mp[i][j] != '.':
				antennas[mp[i][j]] += [(i, j)]
	
	for locs in antennas.values():
		for i in range(len(locs)):
			for j in range(i + 1, len(locs)):
				A1y, A1x = locs[i]   # A for antenna
				A2y, A2x = locs[j]

				dx = A1x - A2x
				dy = A1y - A2y

				B1x = A1x + dx	# B for antinode 
				B1y = A1y + dy
				B2x = A2x - dx
				B2y = A2y - dy

				if 0 <= B1x < m and 0 <= B1y < n:
					antinodes.add((B1y, B1x))
				if 0 <= B2x < m and 0 <= B2y < n:
					antinodes.add((B2y, B2x))
	return len(antinodes)

	
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)