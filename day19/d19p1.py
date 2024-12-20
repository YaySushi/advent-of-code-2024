def read_file_and_answer(file_path):
	patterns = []
	towels = []
	with open(file_path, 'r') as file:
		line = file.readline().strip()
		patterns = line.split(', ')

		line = file.readline().strip()
		line = file.readline().strip()
		while line != "":
			towels.append(line)
			line = file.readline().strip()

	return possible_designs(towels, patterns)

def possible_designs(towels, patterns):
	ans = 0
	
	def make_towel(towel):
		if towel == '': return True
		for patt in patterns:
			patt_len = len(patt)
			if towel.startswith(patt) and make_towel(towel[patt_len:]):
				return True
		return False

	for towel in towels: 
		if make_towel(towel): ans += 1
	return ans


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)