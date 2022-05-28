# Marking Multiples Using Bit Manipulation
import math
def checkbit( array, index):
	return array[index >> 5] & (1 << (index & 31))
def setbit( array, index):
	array[index >> 5] |= (1 << (index & 31))

# Driver Code
a = 2
b = 10
size = abs(b - a)
size = math.ceil(size / 32)
array = [0 for i in range(size)]
for i in range(a, b + 1):
	if (i % 2 == 0 or i % 5 == 0):
		setbit(array, i - a)

print("MULTIPLES of 2 and 5:")
for i in range(a, b + 1):
	if (checkbit(array, i - a)):
		print(i, end = " ")

