n = int(input())

def pattern(n):
	row = 1
	while row <= n:
		col = 1
		while col <= row:
			if col == row or col == 1:
				print(row, end = '\t')
			else:
				print('0', end = '\t')
			col += 1
		print()
		row += 1

pattern(n)