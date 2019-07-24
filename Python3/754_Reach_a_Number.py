# Time: O(n*logn)
# Space: O(1)
"""
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.

Note:
·target will be a non-zero integer in the range [-10^9, 10^9].

在一根无限长的数轴上，你站在0的位置。终点在target的位置。

每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。

返回到达终点需要的最小移动次数。

示例 1:
输入: target = 3
输出: 2
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 3 。

示例 2:
输入: target = 2
输出: 3
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 -1 。
第三次移动，从 -1 到 2 。

注意:
·target是在[-10^9, 10^9]范围中的非零整数。
"""


class Solution:
    # @return an integer
    """
    思路分析:
    1.由于对称性, target正负无影响, 都取正;
    2.从0-target尽量都向右(都取正步数)才能得最优解;
    3.步数都取正, 直到sum>=target;
    4.当sum-target为偶数时, 在前面的(sum-target)/2取负步数即可, 例sum-target=2, 则+1变为-1, 即向左了2步;
    5.向左时无论当前步数是奇是偶, 相当于乘2, 都会变成偶数, 所以只有当(sum-target)为偶数时, 才能通过向左移动使得最终到达target。
    """
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        sum = 0
        res = 1
        while True:
            sum += res
            if sum >= target and (sum - target) % 2 == 0:
                return res
            res += 1


if __name__ == "__main__":
    result = Solution().reachNumber(2)
    print(result)