# Problem: Search Insert Position
# Difficulty: Easy
# Category: Array
# Leetcode 35:https://leetcode.com/problems/search-insert-position/#/description
# Description:
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution(object):
	def searchInsert(self, nums, target):
		"""
	    :param nums: List[int]
	    :param target: int
	    :return: int
	    """
		if len(nums) == 0:
			return None
		if target <= nums[0]:
			return 0
		if target > nums[len(nums) - 1]:
			return len(nums)

		left = 0
		right = len(nums) - 1

		while left < right:
			mid = (left + right) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				left = mid + 1
			else:
				right = mid - 1
		return left


test1 = [1, 3]
test2 = [1, 2, 3, 4, 5, 10]
obj = Solution()
print(obj.searchInsert(test2, 2))
print(obj.searchInsert(test1, 3))