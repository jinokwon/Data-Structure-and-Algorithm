06/11/2020
[Question } Write a function that Finds a subsequence of an array
(Ex) [1, 3, 5] is a subsequence of the array [-1, 1, 2, 3, 4, 5, 6]

[ANS]
def is_sub(array, sequence):
	arr_idx = 0
 	seq_idx = 0
 	while arr_idx < len(array) and seq_idx < len(sequence):
 		if array[arr_idx] == sequence[seq_idx]:
 			seq_idx += 1
 		arr_idx += 1
 	# if the sequence index moved all the way to the last index ('len(sequence)'), it means 'sequence' is a subsequence.
 	return seq_idx == len(sequence)

06/10/2020



06/09/2020
[Question 1] Write a function for the sum of two numbers
input : (1) non-empty array of distinct integers and (2) a target sum
return : any couple of numbers that sum up to the target sum.
(return null if none)

[ANS]
def twoNumberSum(array, targetSum):
	array.sort()
	l = 0
	r = len(array)-1
	while l < r:
		current = array[l] + array[r]
		if current == targetSum:
			return [array[l], array[r]]
		elif current < targetSum:
			l += 1
		elif current > targetSum:
			r -= 1
	return []
