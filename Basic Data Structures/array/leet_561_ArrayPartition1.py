# Problem: Array Partition 1
# Difficulty: Easy
# Category: Array
# Leetcode 561: https://leetcode.com/problems/array-partition-i/
# Description:
"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""


class Solution(object):

	def array_partition_1(self, nums):

		# corner cases
		if len(nums) <= 1:
			return None

		b = []
		n = len(nums)
		for i in range(len(nums)):
			b.append((nums.sort[n-1-i], nums.sort[n-1-i-1]))

		return b

obj = Solution()
testNums = [1, 4, 3, 2]
print(obj.array_partition_1(testNums))
