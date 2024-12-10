def read_file_and_answer(file_path):
	fs = ''
	with open(file_path, 'r') as file:
		for line in file:
			fs = list(line.strip())
	return checksum(fs)

def checksum(fs):
	efs = expand_fs(fs)   # expanded fs (number becomes dots and ids)
	j = len(efs) - 1   # index of last file block index
	
	while j >= 0:
		block_len = len_file_block(efs, j)
		possible_free_index = index_free_space(efs, block_len)
		#print(block_len, possible_free_index)

		if 0 <= possible_free_index < j:
			# move current block to this free space
			for k in range(block_len):
				efs[possible_free_index + k] = efs[j - k]
				efs[j - k] = '.'
		else:
			# move j past the current block that we can't move
			j -= block_len
			
		# shift j back to the end of next block (if required)
		while efs[j] == '.': j -= 1

	cs = 0    # cs for checksum
	for k in range(len(efs)):
		if efs[k] == '.': continue
		cs += k * (ord(efs[k]) + (-1 if ord(efs[k]) > 46 else 0))

	return cs

# expand the fs... LOL
def expand_fs(fs):
	efs = []
	id = 0
	for i in range(len(fs)):
		if i % 2 == 0: 
			if chr(id) == '.': id += 1
			efs += [chr(id)] * int(fs[i])
			id += 1
		else: efs += ['.'] * int(fs[i])
	return efs

# return index of first free space in a sequence 
# of free spaces of length >= l
def index_free_space(efs, l):
	current_l = 0
	for i in range(len(efs)):
		if efs[i] == '.': 
			current_l += 1
			if current_l == l:
				return i - l + 1
		else: current_l = 0
	return -1

# return length of the file block ending at index j
def len_file_block(efs, j):
	id = efs[j]
	l = 0
	while j >= 0 and efs[j] == id: 
		l += 1
		j -= 1
	return l


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)