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
	BOX_L = '['
	BOX_R = ']'
	WALL = '#'

	# convert the map to be twice as wide
	part2_mapping = {
		"#": "##",
		"O": "[]",
		".": "..",
		"@": "@."
	}
	for i in range(n):
		new_row = ''
		for j in range(m):
			new_row += part2_mapping.get(mp[i][j])
		mp[i] = list(new_row)
	m *= 2


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

		# if the robot is moving horizontally, use part 1's logic
		if di == 0:
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
			while mp[i][j] != ROBOT:
				mp[i][j] = mp[i - di][j - dj]
				i, j = i - di, j - dj
			
			# by now, the robot has moved (but we need to clear its old spot on map)
			mp[i][j] = EMPTY

			return (ni, nj)
		# if the robot is moving vertically, recursively check if 
		# the boxes in front of robot can move.
		else:
			# box in front left of robot
			if mp[ni][nj] == BOX_R and can_move_box(ni, nj - 1, di, dj):
				move_box(ni, nj - 1, di, dj)
				# move robot
				mp[ri][rj] = EMPTY
				mp[ni][nj] = ROBOT
				return (ni, nj)
			
			# box in front right of robot
			elif mp[ni][nj] == BOX_L and can_move_box(ni, nj, di, dj):
				move_box(ni, nj, di, dj)
				# move robot
				mp[ri][rj] = EMPTY
				mp[ni][nj] = ROBOT
				return (ni, nj)
			
			# otherwise, did not move robot so return original position
			return (ri, rj)

	# move box on (bi, bj) in direction (di, dj)
	# move any box in front of this box, and so on...
	def move_box(bi, bj, di, dj):
		# next box position.
		nbi, nbj = bi + di, bj + dj

		# two boxes in front
		if mp[nbi][nbj] == BOX_R and mp[nbi][nbj + 1] == BOX_L:
			move_box(nbi, nbj - 1, di, dj)
			move_box(nbi, nbj + 1, di, dj)
		# one box in front left
		elif mp[nbi][nbj] == BOX_R:
			move_box(nbi, nbj - 1, di, dj)
		# one box in front center
		elif mp[nbi][nbj] == BOX_L:
			move_box(nbi, nbj, di, dj)
		# one box in front right
		elif mp[nbi][nbj + 1] == BOX_L:
			move_box(nbi, nbj + 1, di, dj)
		
		# at this point there's no box in front, so move this box
		mp[nbi][nbj] = BOX_L
		mp[nbi][nbj + 1] = BOX_R
		mp[bi][bj] = EMPTY
		mp[bi][bj + 1] = EMPTY

	# return True if the box on (bi, bj) can be moved in the direction (di, dj)
	def can_move_box(bi, bj, di, dj):
		# next box position.
		nbi, nbj = bi + di, bj + dj

		# wall in front of the box:
		if mp[nbi][nbj] == WALL or mp[nbi][nbj + 1] == WALL:
			return False
		# two boxes in front
		elif mp[nbi][nbj] == BOX_R and mp[nbi][nbj + 1] == BOX_L:
			return can_move_box(nbi, nbj - 1, di, dj) and can_move_box(nbi, nbj + 1, di, dj)
		# one box in front left
		elif mp[nbi][nbj] == BOX_R:
			return can_move_box(nbi, nbj - 1, di, dj)
		# one box in front center
		elif mp[nbi][nbj] == BOX_L:
			return can_move_box(nbi, nbj, di, dj)
		# one box in front right
		elif mp[nbi][nbj + 1] == BOX_L:
			return can_move_box(nbi, nbj + 1, di, dj)

		# at this point, no box is in front. 
		return True


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
			if mp[i][j] == BOX_L:
				coord_sum += i * 100 + j
	
	return coord_sum

	
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)