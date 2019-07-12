# Time: O(n)
# Space: O(1)
"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result
equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false
 

Note:
1. 0 <= A.length <= 20000
2. 0 <= B.length <= 20000
3. A and B consist only of lowercase letters.


给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。

示例 1：
输入： A = "ab", B = "ba"
输出： true

示例 2：
输入： A = "ab", B = "ab"
输出： false

示例 3:
输入： A = "aa", B = "aa"
输出： true

示例 4：
输入： A = "aaaaaaabc", B = "aaaaaaacb"
输出： true

示例 5：
输入： A = "", B = "aa"
输出： false
 

提示：
1. 0 <= A.length <= 20000
2. 0 <= B.length <= 20000
3. A 和 B 仅由小写字母构成。
"""


class Solution:
    # @return a boolean
    def buddyStrings(self, A: str, B: str) -> bool:
        """
        思路：
        如果 A[i] == B[i]，我们就说 i 是匹配的，否则称 i 是不匹配的。亲密字符串几乎是完全匹配的，因为一次交换只会影响到两个索引。
        如果交换 A[i] 和 A[j] 可以证明 A 和 B 是亲密字符串，那么就有 A[i] == B[j] 以及 A[j] == B[i]。
        这意味着在 A[i], A[j], B[i], B[j] 这四个自由变量中，只存在两种情况：A[i] == A[j] 或 A[i] != A[j]。
        """
        if len(A) != len(B):
            return False
        if A == B:
            return len(set(A)) < len(B)
        else:
            res = [[i,j] for i,j in zip(A,B) if i != j]
            return res[0][::-1] == res[1] and len(res) == 2


if __name__ == "__main__":
    result = Solution().buddyStrings(A = "aaaaaaabc", B = "aaaaaaacb")
    print(result)