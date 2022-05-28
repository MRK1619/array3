# All Combination Of Size r In An Array Of Size n
def printCombination(arr, n, r):
	
	data = [0]*r;
	combinationUtil(arr, data, 0,
					n - 1, 0, r);
def combinationUtil(arr, data, start,
					end, index, r):
	if (index == r):
		for j in range(r):
			print(data[j], end = " ");
		print();
		return;
	i = start;
	while(i <= end and end - i + 1 >= r - index):
		data[index] = arr[i];
		combinationUtil(arr, data, i + 1,
						end, index + 1, r);
		i += 1;

# Driver Code
arr = [6,8,3,2,7];
r = 3;
n = len(arr);
printCombination(arr, n, r);
