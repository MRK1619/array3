# Find Number Of Operations To Make An array Palidrome.

def findMinOps(arr, n):
	ans = 0 # Initialize Result
	i,j = 0,n-1
	while i<=j:
		if arr[i] == arr[j]:
			i += 1
			j -= 1
		elif arr[i] > arr[j]:
			j -= 1
			arr[j] += arr[j+1]
			ans += 1
		else:
			i += 1
			arr[i] += arr[i-1]
			ans += 1

	return ans
# Driver Program 
arr = [1, 4, 2, 3, 1]
n = len(arr)
print("Count of minimum operations is " + str(findMinOps(arr, n)))
