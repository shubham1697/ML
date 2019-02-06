t = int(input())
while t > 0:
	n = int(input())
	t-=1

	if n == 1:
		print("(0,1)",end = ' ')
		continue

	for a in range(n//2):
		for b in range(a,n//2):
			if (a*a) + (b*b) == n:
				print("(" + str(a) + "," + str(b) + ")",end = ' ')