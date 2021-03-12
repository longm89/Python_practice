"""
You are given coins of different denominations and
a total amount of money amount. Write a function to compute
the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2**31 - 1
0 <= amount <= 10**4
"""


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        """
        Let min_coins[i] be the min number of coins needed to achieve amount i,
        We have len(min_coins) <= amount + 1
        The amount of coins needed if possible is <= amount <= 10**4
        In the beginning, for i != 0, min_coins[i] = 10**5, min_coins[0] = 0
        for total in range(1, amount + 1)
            for coin in coins:
                if total-coin >= 0:
                    min_coins[total] = min(min_coins[total],
                                           min_coins[total - coin] + 1)
   
        The time complexity is O(amount * len(coins))
        The space complexity is O(amount)
        """
        # initialize
        min_coins = [10**5 for i in range(amount + 1)]
        min_coins[0] = 0
        
        # calculate min_coins[total] for total >= 1
        for total in range(1, amount + 1):
            for coin in coins:
                if total-coin >= 0:
                    min_coins[total] = min(min_coins[total],
                                           min_coins[total - coin] + 1)
                                           
        if min_coins[amount] != 10**5:
            return min_coins[amount]
        else:
            return -1
