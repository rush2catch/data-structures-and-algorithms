# Problem: Coin Change
# Difficulty: Medium
# Category: DP
# Leetcode 322: https://leetcode.com/problems/coin-change/description/
"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)
Example 2:
coins = [2], amount = 3
return -1.
Note:
You may assume that you have an infinite number of each kind of coin.
"""


class Solution(object):

	def coin_change(self, coins, amount):


obj = Solution()
coins1 = [1, 2, 5]
coins2 = [2]
coins3 = [2, 5, 10, 20]
coins4 = [186, 419, 83, 408]
print(obj.coin_change(coins1, 11))
print(obj.coin_change(coins2, 3))
print(obj.coin_change(coins3, 16))
print(obj.coin_change(coins4, 6249))
