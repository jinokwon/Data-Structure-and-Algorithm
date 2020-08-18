[Review]
* Array
Static vs Dynamic array:
- dynamic array : Python lists are all dynamic arrays, which means that they automatically manage memory (i.e., when inserting new elements).
- static array : Like in C++ or Java, programmers should allocate and manage memory when making modifications to the array.

* List vs Tuple
- Lists are ordered and mutable ==> Python uses dynamic array by default (unlike in Java where static arrays can be used)
- tuples are NOT mutable.


07/21/2020 - MinMax Stack

class MinMaxStack:
	def __init__(self):
		self.min_max_stack = []
		self.stack = []
		
	def peek(self):
		return self.stack[-1]
	
	def pop(self):
		self.min_max_stack.pop()
		return self.stack.pop()
	
	def push(self, number):
		new_min_max = {"min": number, "max": number}
		if self.min_max_stack:
			last_min_max = self.min_max_stack[-1]
			new_min_max["min"] = min(last_min_max["min"], number)
			new_min_max["max"] = min(last_min_max["max"], number)
		self.min_max_stack.append(new_min_max)
		self.stack.append(number)
	
	def getMin(self):
		return self.min_max_stack[-1]["min"]
	
	def getMax(self):
		return self.min_max_stack[-1]["max"]
	

06/30/2020 - single cycle
[Question 9]
def single_cycle(array):
	num_visited = 0
	current_idx = 0
	while num_visited < len(array):
		if num_visited > 0 and current_idx == 0:
			return False
		current_idx = get_idx(array, current_idx)
		num_visited += 1

def get_idx(array, current_idx):
	next_idx = (current_idx + array[current_idx]) % len(array)
	return next_idx
	
----------------------------------------------------------------------------------------------------
06/25/2020 - Permutations
[Question 8]
def Permutations(array):
	permute = []
	permute_helper(0, array, permute)
	return permute

def permute_helper(i, array, permute):
	if i == len(array) - 1:
		permute.append(array[:])
	else:
		for j in range(i, len(array)):
			array[i], array[j] = array[j], array[i]
			permute_helper(i+1, array, permute)
			array[j], array[i] = array[i], array[j]
* Explanation:
i = 0 -- array: [1, 2, 3]			
	i) j=0 --> i=1 - permut(1, 2, 3) 
	ii) j=1 --> i=1 - permut(2, 1, 3)
	iii) j=2 --> i=1 - permut(3, 2, 1)
i)
i = 1 -- array: [1, 2, 3]
	j=1 --> i=2 - permut(1, 2, 3)
	j=2 --> i=2 - permut(1, 3, 2)
ii)
i = 1 -- array: [2, 1, 3]
	j=1 --> i=2 - permut(2, 1, 3)
	j=2 --> i=2 - permut(2, 3, 1)
i = 1 -- array: [3, 2, 1]
	j=1 --> i=2 - permut(3, 2, 1)
	j=2 --> i=2 - permut(3, 1, 2)
----------------------------------------------------------------------------------------------------
06/23/2020 - Write a function that takens in an array and returns all the possible subsets of it.
[Question 7]
def powerset(array):
	subsets = [[]]
	for element in array:
		for i in range(len(subsets)):
			current_set = subsets[i]
			subsets.append(current_set + [element])
	return subsets
----------------------------------------------------------------------------------------------------
06/18/2020 - Find the sume of three numbers from an array that sum up to the given tager sum.
[Question 6]
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

----------------------------------------------------------------------------------------------------
06/17/2020 - Find three largest numbers from a list
[Question 5]
def findThreeLargestNumbers(array):
	three_large = [None, None, None]
	for num in array:
		largest_helper(three_large, num)
	return three_large

def largest_helper(three_large, num):
	if three_large[2] is None or num > three_large[2]:
		update_helper(three_large, num, 2)
	elif three_large[1] is None or num > three_large[1]:
		update_helper(three_large, num, 1)
	elif three_large[0] is None or num > three_large[0]:
		update_helper(three_large, num, 0)

def update_helper(array, num, idx):
	for i in range(idx+1):
		if i == idx:
			array[i] = num
		else:
			array[i] = array[i+1]

----------------------------------------------------------------------------------------------------
06/15/2020 - Insertion Sort & Selection Sort
[Question 4]
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
----------------------------------------------------------------------------------------------------
06/13/2020
[Question 3] Write a function that Finds a subsequence of an array
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
----------------------------------------------------------------------------------------------------
06/11/2020
[Question 2] Write a function that Finds a subsequence of an array
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
----------------------------------------------------------------------------------------------------
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
