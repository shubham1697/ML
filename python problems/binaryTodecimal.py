bin = int(input())
dec = 0
n =0 
while bin > 0:
	rem = bin % 10
	dec += rem * (2 ** n)
	n += 1
	bin = bin // 10

print(dec)