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
	saved_towels = {}
	ans = 0

	def make_towel(towel):
		if towel == '': return 1

		if towel in saved_towels: return saved_towels[towel]
		
		count_so_far = 0
		for patt in patterns:
			patt_len = len(patt)
			if towel.startswith(patt):
				count_so_far += make_towel(towel[patt_len:])
		
		saved_towels[towel] = count_so_far
		return count_so_far

	for towel in towels: 
		ans += make_towel(towel)
	return ans


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)