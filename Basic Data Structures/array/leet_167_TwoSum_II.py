# Problem: Two Sum II - input array is sorted
# Difficulty: Easy
# Category: Array/Hash Table
# Leetcode 167: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description
# Description:
"""
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
class Solution(object):

	# hash table solution
	def two_sum_1(self, nums, target):
		buff = {}
		for i in range(len(nums)):
			if target - nums[i] in buff:
				return [buff[target - nums[i]], i]
			else:
				buff[nums[i]] = i

	# two pointer


	# binary search

obj = Solution()
testNums1 = [2, 7, 11, 15]
print(obj.two_sum(testNums1, 9))