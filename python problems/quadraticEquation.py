a = int(input())
b = int(input())
c = int(input())

def quadraticEq(a, b, c):
	D = b**2 - 4*a*c
	if D < 0:
		print("Imaginary")
	else:
		r = int((-b - D**0.5)/2*a)
		s = int((-b + D**0.5)/2*a)

		if r == s:
			print("Real and Equal")
		else:
			print("Real and Distinct")

		print(r,s, sep = ' ')
quadraticEq(a, b, c)