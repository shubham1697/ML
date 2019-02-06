n = int(input())

def pattern(n):
	row = 1
	nsp = n + 1
	while row <= n:
		col = 1
		csp = 1
		while col <= row:
			print(col,end = '\t')
			col += 1

		col = row
		if row == n:
			col = row - 1

		while csp <= nsp:
			print(' ', end = '\t')
			csp += 1

		while col > 0:
			print(col, end = '\t')
			col -= 1

		print()
		row += 1
		nsp -= 2

pattern(n)