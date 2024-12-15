def read_file_and_answer(file_path):
	# mp for map because map is taken :(
	mp = []
	moves = ''
	with open(file_path, 'r') as file:
		for line in file:
			line_stripped = line.strip()
			if len(line_stripped) > 0 and line_stripped[0] == '#':
				mp.append(list(line_stripped))
			else:
				moves = moves + line_stripped
	return box_gps(mp, moves)

def box_gps(mp, moves):
	n = len(mp)
	m = len(mp[0])
	dirs = {
		'^': (-1, 0), 
		'>': (0, 1), 
		'v': (1, 0), 
		'<': (0, -1)
	}
	ROBOT = '@'
	EMPTY = '.'
	BOX = 'O'
	WALL = '#'


	# move the robot on (ri, rj) in the direction (ni, nj)
	# return new robot position
	def move_robot(ri, rj, di, dj):
		# ni means "next i"
		ni, nj = ri + di, rj + dj

		# move into empty space:
		if mp[ni][nj] == EMPTY:
			# update map
			mp[ni][nj] = ROBOT
			mp[ri][rj] = EMPTY

			# return new robot position
			return (ni, nj)
		
		# move into wall:
		if mp[ni][nj] == WALL: return (ri, rj)

		# otherwise, moving into a box.

		# check if the sequence of boxes starting from this box
		#    in the direction (di, dj) can be moved
		# i.e. is there an empty space between robot and the first 
		#    wall in the direction (di, dj)

		i, j = ni, nj
		while mp[i][j] != WALL and mp[i][j] != EMPTY:
			i, j = i + di, j + dj
		
		# (i, j) either contains a wall or is empty at this point

		# if it is a wall, the boxes between robot and this wall 
		#    can not be moved.
		if mp[i][j] == WALL: return (ri, rj)

		# otherwise all the boxes shift one in the direction (di, dj)
		# this can be done by moving the next box over to the empty spot
		mp[i][j] = BOX
		mp[ri][rj] = EMPTY
		mp[ni][nj] = ROBOT

		return (ni, nj)
		
	# find starting position of robot
	# ri means "robot i"
	ri, rj = -1, -1
	for i in range(n):
		for j in range(m):
			if mp[i][j] == ROBOT:
				ri, rj = i, j

	# iteratively apply each move
	for move in moves:
		# di means "delta i", i.e. change in i direction
		(di, dj) = dirs[move]
		ri, rj = move_robot(ri, rj, di, dj)

	# find some of coordinates
	coord_sum = 0
	for i in range(n):
		for j in range(m):
			if mp[i][j] == BOX:
				coord_sum += i * 100 + j
	
	return coord_sum

	
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)