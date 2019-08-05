"""
Implement a trie with insert, search, and startsWith methods.

Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

Note:
·You may assume that all inputs are consist of lowercase letters a-z.
·All inputs are guaranteed to be non-empty strings.

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true

说明:
·你可以假设所有的输入都是由小写字母 a-z 构成的。
·保证所有输入均为非空字符串。
"""


class Trie:
    # 思路: 字典按字母迭代

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # @return None
        # Time: O(m)
        # Space: O(m)
        a=self.dic
        for i in word:
            if not i in a:
                a[i]={}
            a=a[i]
        a["end"]=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # @return a boolean
        # Time: O(m)
        # Space: O(1)
        a=self.dic
        for i in word:
            if not i in a:
                return False
            a=a[i]
        if "end" in a:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # @return a boolean
        # Time: O(m)
        # Space: O(1)
        a=self.dic
        for i in prefix:
            if not i in a:
                return False
            a=a[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == "__main__":
    obj = Trie()
    obj.insert("apple")
    print(obj.search("apple"))
    print(obj.search("app"))
    print(obj.startsWith("app"))
    obj.insert("app")
    print(obj.search("app"))