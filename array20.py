#  The Longest Subarray With Sum Divisible By K
def longestSubarrWthSumDivByK(arr, n, k):

	# Unordered Map 'um' Implemented As Hash Table
	um = {}

	max_len = 0
	curr_sum = 0

	for i in range(n):
	
		curr_sum += arr[i]
		mod = ((curr_sum % k) + k) % k
		if mod == 0:
			max_len = i + 1
		elif mod in um.keys():
			if max_len < (i - um[mod]):
				max_len = i - um[mod]

		else:
			um[mod] = i
	return max_len

arr = [2, 8, 6, 3, 4, 9]
n = len(arr)
k = 3
print("Length =", longestSubarrWthSumDivByK(arr, n, k))

