def read_file_and_answer(file_path):
    codes = []
    with open(file_path, 'r') as file:
        for line in file:
            if line != '': 
                   codes.append(line.strip())
    return complexities_sum(codes)

def complexities_sum(codes):
    complexity = 0
    for code in codes:
        seqs = keypad_moves(keypad_moves(keypad_moves([code])))

        num = int(code[:3])
        min_seq_len = float('inf')

        for seq in seqs:
            min_seq_len = min(min_seq_len, len(seq))
        
        complexity += min_seq_len * num
    
    return complexity

def keypad_moves(key_seqs):
    prev_key = 'A'
    ans = []
    for seq in key_seqs:
        # perform calculation for each sequence. return answer for each seq
        seq_moves = ['']
        for key in seq:
            # go through each key in this sequence.

            # how many ways can we move from prev_key to this key?
            all_key_to_key_moves = key_to_key_moves(prev_key, key)
            
            # update seq moves list at each step.
            new_seq_moves = []
            for moves in seq_moves:
                # for each of the old moves, append each of the all_key_to_key_moves elements to it.
                for x in all_key_to_key_moves:
                    new_seq_moves.append(moves + x)
            
            # set seq_moves to be new_seq_moves
            seq_moves = new_seq_moves

            # make this the prev_key for next iteration
            prev_key = key
        ans += seq_moves
    
    return ans

def key_loc(key):
    # These are the keypads used. 
    # +---+---+---+
    # | 7 | 8 | 9 |
    # +---+---+---+
    # | 4 | 5 | 6 |
    # +---+---+---+
    # | 1 | 2 | 3 |
    # +---+---+---+
    #     | 0 | A |
    #     +---+---+
    #     +---+---+
    #     | ^ | A |
    # +---+---+---+
    # | < | v | > |
    # +---+---+---+

    # We will overlap the top row of the directional keypad with
    # the bottom row of the numerical key pad.
     
    key_loc_map = {
        '7': (0, 0),
        '8': (0, 1),
        '9': (0, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '1': (2, 0),
        '2': (2, 1),
        '3': (2, 2),
        '0': (3, 1),
        '^': (3, 1),
        'A': (3, 2),
        '<': (4, 0),
        'v': (4, 1),
        '>': (4, 2),
    }
    return key_loc_map[key]

def key_to_key_moves(key1, key2):
    horizontal_moves = ''
    vertical_moves = ''

    r1, c1 = key_loc(key1)
    r2, c2 = key_loc(key2)

    # r2 > r1: moving downwards
    if r2 > r1: vertical_moves += 'v' * (r2 - r1)
    else: vertical_moves += '^' * (r1 - r2)
    
    # c2 > c1: moving rightwards
    if c2 > c1: horizontal_moves += '>' * (c2 - c1)
    else: horizontal_moves += '<' * (c1 - c2)

    # handle cases where we could cross the empty space if we include 
    # two ways of getting to the next button
    if key1 in {'<', '1', '4', '7'} and key2 in {'^', 'A', '0'}:
        return [horizontal_moves + vertical_moves + 'A']
    if key2 in {'<', '1', '4', '7'} and key1 in {'^', 'A', '0'}:
        return [vertical_moves + horizontal_moves + 'A']
    
    # otherwise, no worries about crossing an empty space

    # if there's two ways to get to the next buttom, return both.
    if horizontal_moves != '' and vertical_moves != '':
        return [
            horizontal_moves + vertical_moves + 'A',
            vertical_moves + horizontal_moves + 'A'
        ]
    
    # only one way. return that single way
    return [vertical_moves + horizontal_moves + 'A']


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)