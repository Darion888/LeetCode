# Time: O(Sn)
# Space: O(S)
# S: 金额
# n: 面额数
"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest
number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the
coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1

说明:
你可以认为每种硬币的数量是无限的。
"""
from typing import List


class Solution:
    # @return an integer
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 思路: BFS广度优先搜索算法
        if amount == 0:
            return 0
        value1 = []
        value2 = [0]
        nc = 0
        visited = [False] * (amount + 1)
        visited[0] = True
        while value2:
            nc += 1
            for v in value2:
                for c in coins:
                    newValue = v + c
                    if newValue == amount:
                        return nc
                    elif newValue > amount:
                        continue
                    elif not visited[newValue]:
                        visited[newValue] = True
                        value1.append(newValue)
            value1, value2 = [], value1
        return -1


class Solution2:
    # @return an integer
    # 思路: 动态规划
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [0 for _ in range(amount + 1)]

        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, res[i - c] + 1)
            res[i] = cost

        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]


if __name__ == "__main__":
    result = Solution().coinChange(coins = [1, 2, 5], amount = 11)
    result2 = Solution2().coinChange(coins = [1, 2, 5], amount = 11)
    print(result)
    print(result2)