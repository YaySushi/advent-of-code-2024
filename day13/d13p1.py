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
			Px = int(line.split('=')[1].split(',')[0])
			Py = int(line.split('=')[2])

			line = file.readline().strip()
			line = file.readline().strip()

			machines.append(((Ax, Ay), (Bx, By), (Px, Py)))

	return token_count(machines)

def token_count(machines):
	total_tokens = 0
	for ((Ax, Ay), (Bx, By), (Px, Py)) in machines:
		min_tokens = float('inf')   # haha
		for i in range(101):  # given: no more than 100 presses on any button
			# can press B correct number of times to get Px
			if (Px - (i * Ax)) % Bx != 0: continue

			# can press B correct number of times to get Py
			if (Py - (i * Ay)) % By != 0: continue

			# in each case, B should be pressed same number of times
			if (Px - (i * Ax)) // Bx != (Py - (i * Ay)) // By: continue
			Acount = i
			Bcount = (Px - (i * Ax)) // Bx
			tokens = Acount * 3 + Bcount

			if tokens < min_tokens: min_tokens = tokens
		if min_tokens != float('inf'): total_tokens += min_tokens

	return total_tokens


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)