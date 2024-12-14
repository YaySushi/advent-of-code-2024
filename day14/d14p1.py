from functools import reduce

def read_file_and_answer(file_path):
	# mp for map because map is taken :(
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
	seconds = 100
	n = 103
	m = 101

	def move(robo):
		px, py = robo['pos']
		vx, vy = robo['vel']
		px = (px + vx) % m
		py = (py + vy) % n
		robo['pos'] = (px, py)
		return robo


	for k in range(seconds): robos = list(map(move, robos))
	
	qs = [0] * 4

	for robo in robos:
		i, j = robo['pos']
		if i < 50 and j < 51: qs[0] += 1
		if i < 50 and 52 <= j: qs[1] += 1
		if 51 <= i and j < 51: qs[2] += 1
		if 51 <= i and 52 <= j: qs[3] += 1

	return reduce (lambda a, b: a * b, qs, 1)

	
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)