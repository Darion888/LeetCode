"""
Implement the following operations of a queue using stacks.
·push(x) -- Push element x to the back of queue.
·pop() -- Removes the element from in front of queue.
·peek() -- Get the front element.
·empty() -- Return whether the queue is empty.

Example:
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:
·You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
·Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
·You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

使用栈实现队列的下列操作：

·push(x) -- 将一个元素放入队列的尾部。
·pop() -- 从队列首部移除元素。
·peek() -- 返回队列首部的元素。
·empty() -- 返回队列是否为空。

示例:
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

说明:
·你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
·你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
·假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # Time: O(n)
        # Space: O(n)
        # 两个栈倒，新来的元素总是在栈底（队尾进）
        if self.stack1 == None:
            self.stack1.append(x)
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
            self.stack1.append(x)
            while self.stack2:
                self.stack1.append(self.stack2.pop(-1))

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # Time: O(1)
        # Space: O(1)
        # 直接弹出，因为本来就是队头出
        return self.stack1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        # Time: O(1)
        # Space: O(1)
        if self.stack1:
            return self.stack1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # Time: O(1)
        # Space: O(1)
        # 因为队列１存储了所有元素，所以只需要判断队列１
        return len(self.stack1) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())