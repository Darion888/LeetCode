# Time: O(N^2·logN)
# Space: O(N)
"""
A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

Examples:
Input: A = [1, 2, 3, 5], K = 3
Output: [2, 5]
Explanation:
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

Input: A = [1, 7], K = 1
Output: [1, 7]

Note:
·A will have length between 2 and 2000.
·Each A[i] will be between 1 and 30000.
·K will be between 1 and A.length * (A.length - 1) / 2.

一个已排序好的表 A，其包含 1 和其他一些素数.  当列表中的每一个 p<q 时，我们可以构造一个分数 p/q 。

那么第 k 个最小的分数是多少呢?  以整数数组的形式返回你的答案, 这里 answer[0] = p 且 answer[1] = q.

示例:
输入: A = [1, 2, 3, 5], K = 3
输出: [2, 5]
解释:
已构造好的分数,排序后如下所示:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
很明显第三个最小的分数是 2/5.

输入: A = [1, 7], K = 1
输出: [1, 7]

注意:
·A 的取值范围在 2 — 2000.
·每个 A[i] 的值在 1 —30000.
·K 取值范围为 1 —A.length * (A.length - 1) / 2
"""
from typing import List


class Solution:
    # @return a List[int]
    # 思路: 堆排序

    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        from heapq import heappush ,heappop
        H = []
        N = len(A)
        A = sorted(A)
        for i in range(N):
            for j in range(N-1, i, -1):
                if len(H) < K:
                    heappush(H, (-A[i]/A[j], i , j))
                else:
                    if A[i]/A[j] >= -H[0][0]:
                        break
                    else:
                        heappop(H)
                        heappush(H, (-A[i]/A[j], i, j ))
        return [A[H[0][1]], A[H[0][2]]]


if __name__ == "__main__":
    result = Solution().kthSmallestPrimeFraction(A = [1, 2, 3, 5], K = 3)
    print(result)