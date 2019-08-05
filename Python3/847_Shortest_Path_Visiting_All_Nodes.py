# Time: O(N^4)
# Space: O(N)
"""
An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes
multiple times, and you may reuse edges.

Example 1:
Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Example 2:
Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]

Note:
·1 <= graph.length <= 12
·0 <= graph[i].length < graph.length

给出 graph 为有 N 个节点（编号为 0, 1, 2, ..., N-1）的无向连通图。 

graph.length = N，且只有节点 i 和 j 连通时，j != i 在列表 graph[i] 中恰好出现一次。

返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。

示例 1：
输入：[[1,2,3],[0],[0],[0]]
输出：4
解释：一个可能的路径为 [1,0,2,0,3]

示例 2：
输入：[[1],[0,2,4],[1,3,4],[2],[1,2]]
输出：4
解释：一个可能的路径为 [0,1,4,2,3]

提示：
·1 <= graph.length <= 12
·0 <= graph[i].length < graph.length
"""
from typing import List


class Solution:
    # @return an integer
    # 思路: 宽搜

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1 and graph[0] == []:
            return 0
        tar = (1 << n) - 1
        ans = float('inf')

        def f(i):
            dic = {(i, 1 << i)}  # 状态记录
            que = {(i, 1 << i)}  # 宽搜队列
            tans = 1  # 临时步长记录
            while que:
                tmp = set()
                for j, t in que:  # que宽搜队列中，j节点，t已访问过的状态
                    for k in graph[j]:  # 遍历j节点的联通点
                        p = t | (1 << k)  # 对节点进行访问
                        if p == tar:  # 如果全部访问，就统计最短的临时步长
                            nonlocal ans
                            ans = min(ans, tans)
                            return
                        if (k, p) not in dic:  # 不进入重复的状态
                            dic |= {(k, p)}
                            tmp |= {(k, p)}
                que = tmp
                tans += 1

        for i in range(n): f(i)  # 从各个节点开始走

        return ans


if __name__ == "__main__":
    result = Solution().shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]])
    print(result)