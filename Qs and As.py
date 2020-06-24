06/23/2020 - Write a function that takens in an array and returns all the possible subsets of it.
def powerset(array):
	subsets = [[]]
	for element in array:
		for i in range(len(subsets)):
			current_set = subsets[i]
			subsets.append(current_set + [element])
	return subsets

06/18/2020 - Find the sume of three numbers from an array that sum up to the given tager sum.
def SumofThree(array, targetSum):
	array.sort()
	triple_list = []
	for i in range(len(array)-2):
		left = i+1
		right = len(array) - 1
		while left < right:
			current_sum = array[i] + array[left] + array[right]
			if current_sum == targetSum:
				triple_list.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif current_sum < targetSum:
				left += 1
			elif current_sum > targetSum:
				right -= 1
	return triple_list

06/17/2020 - Find three largest numbers from a list
* Solution 1
def findThreeLargestNumbers(array):
    three_large = [None, None, None]
    cnt = 2
    large_list = []
    while cnt > -1:
        large = 0
        for i in range(1, len(array)):
            if array[i] > array[large] and i not in large_list:
                large = i
            large_list.append(large)
            three_large[cnt] = array[large]
            cnt -= 1
    return three_large

------------------------

06/15/2020 - Insertion Sort & Selection Sort
* Selection Sort
def selection_sort(array):
	sorted_idx = 0
	while sorted_idx < len(array) - 1:
		small_idx = sorted_idx
		for i in range(sorted_idx, len(array)):
			if array[small_idx] > array[i]:
				small_idx = i
		array[sorted_idx], array[small_idx] = array[small_idx], array[sorted_idx]
		sorted_idx += 1
	return array

* Insertion Sort
def insertion_sort(array):
	for i in range(1, len(array)):
		while i !=0:
			if array[i-1] > array[i]:
				array[i-1], array[i] = array[i], array[i-1]
			i -= 1
	return array

06/13/2020
[Question } Write a function that Finds a subsequence of an array
(Ex) [1, 3, 5] is a subsequence of the array [-1, 1, 2, 3, 4, 5, 6]

[ANS]
from string import ascii_lowercase
num_dict = {i:v for (i, v) in enumerate(ascii_lowercase)}
dict_num = {v:i for (i, v) in enumerate(ascii_lowercase)}

def caesar(string, key):
	answer = []
 	for i in string:
 		withKey = dict_num[i] + key % 26
 		if withKey <=25:
 			answer.append(num_dict[withKey])
 		else:
 			answer.append(num_dict[withKey-26])
 	return " ".join(answer)

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
