def read_file_and_answer(file_path):
	machines = []
	with open(file_path, 'r') as file:
		line = file.readline().strip()
		while line != "":
			Ax = int(line.split('+')[1].split(',')[0])
			Ay = int(line.split('+')[2])

			line = file.readline().strip()
			Bx = int(line.split('+')[1].split(',')[0])
			By = int(line.split('+')[2])

			line = file.readline().strip()
			Px = int(line.split('=')[1].split(',')[0]) + 10000000000000
			Py = int(line.split('=')[2]) + 10000000000000

			line = file.readline().strip()
			line = file.readline().strip()

			machines.append(((Ax, Ay), (Bx, By), (Px, Py)))

	return token_count(machines)

def token_count(machines):
	total_tokens = 0
	# Okay this could have just been done with a system in part 1...

	for ((Ax, Ay), (Bx, By), (Px, Py)) in machines:
		# [Ax Bx][i]  =  [Px]
		# [Ay By][j]  =  [Py]
		# 1 / det = 1 / (Ax*By - Ay*Bx)
		det = Ax*By - Ay*Bx

		if det == 0: continue

		factor = 1 / det

		a = factor * By
		b = -factor * Bx
		c = -factor * Ay
		d = factor * Ax

		i = a * Px + b * Py
		j = c * Px + d * Py

		threshold = 0.0001
		if abs(i - round(i)) < threshold and abs(j - round(j)) < threshold:
			total_tokens += 3 * round(i) + round(j)

	return total_tokens


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)