"""
155. Min Stack Add to List
DescriptionSubmissionsSolutions
Total Accepted: 118351
Total Submissions: 434664
Difficulty: Easy
Contributors: Admin
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
Hide Company Tags Google Uber Zenefits Amazon Snapchat Bloomberg
Hide Tags Stack Design
Hide Similar Problems (H) Sliding Window Maximum

"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.st_min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.st_min:
            self.st_min.append(x)
        else:
            self.st_min.append(min(x, self.st_min[-1]))

    def pop(self):
        """
        :rtype: void
        """

        if self.stack:
            self.stack.pop()
            self.st_min.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.st_min:
            return self.st_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
