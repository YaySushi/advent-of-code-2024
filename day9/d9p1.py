def read_file_and_answer(file_path):
	fs = ''
	with open(file_path, 'r') as file:
		for line in file:
			fs = line.strip()
	return checksum(fs)

def checksum(fs):
	efs = ''   # expanded file system (number becomes dots and ids)
	cfs = ''   # compact file system (blocks are moved)
	id = 0

	for i in range(len(fs)):
		if i % 2 == 0: 
			if chr(id) == '.': id += 1
			efs = efs + (chr(id) * int(fs[i]))
			id += 1
		else: 
			efs = efs + ('.' * int(fs[i]))

	j = len(efs) - 1   # index of last file block
	i = 0  # index of starting (current) file block
	
	while i <= j:
		if efs[i] == '.':
			if efs[j] == '.': 
				j -= 1
				continue
			else:
				cfs = cfs + efs[j]
				j -= 1
		else: cfs = cfs + efs[i]
		i += 1

	cs = 0    # cs for checksum
	for k in range(len(cfs)):
		cs += k * (ord(cfs[k]) + (-1 if ord(cfs[k]) > 46 else 0))

	return cs


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)