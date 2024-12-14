def read_file_and_answer(file_path):
	robos = []
	with open(file_path, 'r') as file:
		for line in file:
			[px, py] = list(map(int, line.split()[0][2:].split(',')))
			[vx, vy] = list(map(int, line.split()[1][2:].split(',')))
			robos.append({
				'pos': (px, py),
				'vel': (vx, vy)
			})
	return safety_factor(robos)

def safety_factor(robos):
	n = 103
	m = 101

	def move(robo):
		px, py = robo['pos']
		vx, vy = robo['vel']
		px = (px + vx) % m
		py = (py + vy) % n
		robo['pos'] = (px, py)
		return robo

	f = open('looking_for_easter_egg.txt','w')

	for k in range(100000):   # hopefully it's in here.
		robos = list(map(move, robos))
		for i in range(n):
			row_robos = 0
			for j in range(m):
				robo_present = False
				for robo in robos:
					x, y = robo['pos']
					if j == x and i == y: robo_present = True

				if robo_present: print('X', end='', file=f)
				else: print(' ', end='', file=f)

				if robo_present: row_robos += 1
				else: row_robos = 0

				# this should hopefully have a tree (its base at least)
				if row_robos >= 10: return k + 1
			print('', file=f)
		print(str(k) + '=' * 101, file=f)

	return -1

	
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)