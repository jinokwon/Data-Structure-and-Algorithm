06/10/2020


06/09/2020
Question 1. Write a function for the sum of two numbers
input : (1) non-empty array of distinct integers and (2) a target sum
return : any couple of numbers that sum up to the target sum.
(return null if none)

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
