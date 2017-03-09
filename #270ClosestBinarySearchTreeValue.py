"""
270. Closest Binary Search Tree Value   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 27396
Total Submissions: 71642
Difficulty: Easy
Contributors: Admin
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Hide Company Tags Microsoft Google Snapchat
Hide Tags Tree Binary Search
Hide Similar Problems (M) Count Complete Tree Nodes (H) Closest Binary Search Tree Value II

"""


class Solution(object):

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None

        result, diff = self.helper(root, target)
        return result

    def helper(self, root, target):
        result = root.val
        diff = abs(root.val - target)

        if target >= root.val:
            if root.right:
                rightResult, rightDiff = self.helper(root.right, target)
                if diff > rightDiff:
                    result = rightResult
                    diff = rightDiff
        else:
            if root.left:
                leftResult, leftDiff = self.helper(root.left, target)
                if diff > leftDiff:
                    result = leftResult
                    diff = leftDiff
        return result, diff
