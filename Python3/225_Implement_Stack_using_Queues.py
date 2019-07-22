"""
Implement the following operations of a stack using queues.

·push(x) -- Push element x onto stack.
·pop() -- Removes the element on top of the stack.
·top() -- Get the top element.
·empty() -- Return whether the stack is empty.

Example:
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

Notes:
·You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
·Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
·You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

使用队列实现栈的下列操作：

·push(x) -- 元素 x 入栈
·pop() -- 移除栈顶元素
·top() -- 获取栈顶元素
·empty() -- 返回栈是否为空

注意:
·你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
·你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
·你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        # Time: O(n)
        # Space: O(1)
        if not self.queue1 and not self.queue2:
            self.queue1.append(x)
        elif self.queue1:
            self.queue1.append(x)
        elif self.queue2:
            self.queue2.append(x)
        else:
            return False

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # Time: O(1)
        # Space: O(1)
        if self.queue1:
            for i in range(1, len(self.queue1)):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        else:
            for i in range(1, len(self.queue2)):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        # Time: O(1)
        # Space: O(1)
        if self.queue1:
            for i in range(1, len(self.queue1)):
                self.queue2.append(self.queue1.pop(0))
            top = self.queue1.pop(0)
            self.queue2.append(top)
            return top
        else:
            for i in range(1, len(self.queue2)):
                self.queue1.append(self.queue2.pop(0))
            top = self.queue2.pop(0)
            self.queue1.append(top)
            return top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        # Time: O(1)
        # Space: O(1)
        if not self.queue1 and not self.queue2:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.empty())