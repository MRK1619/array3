#Compute Sum Of Ranges For Different Range Queries
import math
def queryResults(arr,Q):
	Q.sort(key=lambda x: x[1])
	currL,currR,currSum = 0,0,0
	for i in range(len(Q)):
		L,R = Q[i] 
		while currL<L:
			currSum-=arr[currL]
			currL+=1
		while currL>L:
			currSum+=arr[currL-1]
			currL-=1
		while currR<=R:
			currSum+=arr[currR]
			currR+=1
		while currR>R+1:
			currSum-=arr[currR-1]
			currR-=1
		print("Sum of",Q[i],"is",currSum)

arr = [5, 4, 5, 4, 7, 9, 7, 6, 8]
Q = [[0, 3], [2, 3], [2, 5]]
queryResults(arr,Q)

