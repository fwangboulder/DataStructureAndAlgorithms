"""
96. Unique Binary Search Trees Add to List
Description  Submission  Solutions
Total Accepted: 110874
Total Submissions: 276861
Difficulty: Medium
Contributors: Admin
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
Hide Company Tags Snapchat
Hide Tags Tree Dynamic Programming
Hide Similar Problems (M) Unique Binary Search Trees II

Suppose the number of solution with n is f(n). Then for n, the possible cases
for root are 1, 2,..., n. For any root, i, f(i) = f(i-1) * f(n-i) since there
are (i-1) number in the left subtree, and (n-i) number in the right subtree.
Note that if i-1== 0 (or n-i==0), f(i)=f(n-i) (or f(i-1)).

Another thing to mention is DON'T use recursive calls in such problems.
Although it will give you correct answer, it will exceed time limit

"""


class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        num = [0] * (n + 1)
        num[0:3] = [0, 1, 2]

        for i in range(3, n + 1):
            for j in range(2, i):
                num[i] += num[j - 1] * num[i - j]
            num[i] += num[i - 1] * 2

        return num[n]
