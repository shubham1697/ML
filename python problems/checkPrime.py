n = int(input())
flag = 0

for i in range(2,n):
	if n%i == 0:
		flag = 1

if n < 2:
	flag = 1
	
if flag == 1:
	print("Not Prime")
else:
	print("Prime")