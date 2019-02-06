ASCII_SIZE = 256
count = [0] * ASCII_SIZE

str = input()

def MaxFreqChar(str):
	for i in str:
		count[ord(i)] += 1

	max = -1
	for i in str:
		if max < count[ord(i)]:
			max = count[ord(i)]
			c = i

	return c

print(MaxFreqChar(str))