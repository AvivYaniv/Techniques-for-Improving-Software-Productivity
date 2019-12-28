# coding=utf-8

"""
Kakuro exercise.
"""

from z3 import *

def parse_empty_cell(board, row, col, current_cell):
	if (current_cell == 0):
		return board[row][col]
	return current_cell.as_long()

def get_kakuro_solution(board, nrows, ncols):
    s = Solver()

    # Cell variables
    out_board = [[Int('cell_{}_{}'.format(row, col)) for col in range(ncols)] for row in range(nrows)]

    # Cell constraints
    for row in range(nrows):
        for col in range(ncols):
			if (board[row][col] == 'W'):
				s.add(And(out_board[row][col] > 0, out_board[row][col] <= 9))
			else:
				s.add(out_board[row][col] == 0)
	
	# Row sum sgement constraints
	for row in range(nrows):
		row_sum = 0
		row_segment = []
		for col in range(ncols):
			cell = board[row][col]
			if (type(cell) is tuple):
				if (row_sum != 0):
					s.add(Distinct(row_segment))
					s.add(row_sum == Sum(row_segment))
				if (cell[1] != 'B'):
					row_sum = cell[1]
					row_segment = []
			elif (cell == 'W'):
				row_segment.append(out_board[row][col])

		if (row_sum != 0):
			s.add(Distinct(row_segment))
		s.add(row_sum == Sum(row_segment))
		
	# Column sum sgement constraints
	for col in range(ncols):
		col_sum = 0
		col_segment = []
		for row in range(nrows):
			cell = board[row][col]	
			if (type(cell) is tuple):
				if (col_sum != 0):
					s.add(Distinct(col_segment))
					s.add(col_sum == Sum(col_segment))
				if (cell[0] != 'B'):
					col_sum = cell[0]
					col_segment = []
			elif cell == 'W':
				col_segment.append(out_board[row][col])

		if (col_sum != 0):
			s.add(Distinct(col_segment))
			s.add(col_sum == Sum(col_segment))
	
	#print "Solver is:"
	#print s
	#print
	
	print "Checking SAT"
    res = s.check()
    if res == unsat:
        print "UNSAT, No solution."
        return None
    elif res == unknown:
        print "Unknown ¯\\_(ツ)_/¯"
        return None
    else:
        assert res == sat
        print "SAT, Found solution!"
        m = s.model()
        x =  [[parse_empty_cell(board, row, col, m[out_board[row][col]]) for col in range(ncols)] for row in range(nrows)]
        print x
        return x

def draw_board(board, nrows, ncols):
    top = ['┌'] + ['────────────┬' for k in range(ncols-1)] + ['────────────┐'];
    print ''.join(top)
    
    for i in range(nrows):
        print '│',
        for j in range(ncols):
			cell = board[i][j]
			if cell == 'W':
				print '           │',
			elif cell == 'B':
				print '     B     │',
			elif (type(cell) is tuple):
				d,l = cell
				print ' {:>4}\{:<4} │'.format(d,l),
			else: # integer value
				assert type(cell) is int
				print '     {}     │'.format(cell),
        print
        mid = ['├'] + ['────────────┼' for k in range(ncols-1)] + ['────────────┤']
        bottom = ['└'] + ['────────────┴' for k in range(ncols-1)] + ['────────────┘']        
        print ''.join(mid) if i < nrows - 1 else ''.join(bottom)

if __name__ == '__main__':
	# Example 5x5 Input
	board = [
			['B', (16,'B'), (12, 'B'), (29, 'B'), 'B'],
			[('B',23), 'W', 'W', 'W', 'B'],
			[('B', 14), 'W', 'W', 'W', (14, 'B')],
			['B', ('B', 19), 'W', 'W', 'W'],
			['B', ('B', 15), 'W', 'W', 'W']
	]
	#draw_board(board, 5, 5)
	#solution = get_kakuro_solution(board, 5, 5)
	#draw_board(solution, 5, 5)
    
	# # Output:
    # solution = [
    #     ['B', (16, 'B'), (12, 'B'), (29, 'B'), 'B'],
    #     [('B', 23), 9, 6, 8, 'B'],
    #     [('B', 14), 7, 2, 5, (14, 'B')],
    #     ['B', ('B', 19), 3, 7, 9],
    #     ['B', ('B', 15), 1, 9, 5]
    # ]
	
	board = [
		['B','B','B',(13, 'B'),(9, 'B')],
		['B','B',(14,17),'W','W'],
		['B',(10,12),'W','W','W'],
		[('B',8),'W','W','W','B'],
		[('B',4),'W','W','B','B'],
		[('B',5),'W','W','B','B'],
	]

	draw_board(board, 6, 5)
	solution = get_kakuro_solution(board, 6, 5)
	draw_board(solution, 6, 5)
    # # Output:
    # solution = [
    #     ['B', 'B', 'B', (13, 'B'), (9, 'B')],
    #     ['B', 'B', (14, 17), 9, 8],
    #     ['B', (10, 12), 8, 3, 1],
    #     [('B', 8), 5, 2, 1, 'B'],
    #     [('B', 4), 3, 1, 'B', 'B'],
    #     [('B', 5), 2, 3, 'B', 'B']
    # ]
	
    
