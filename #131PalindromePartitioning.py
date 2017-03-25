"""
131. Palindrome Partitioning Add to List
DescriptionSubmissionsSolutions
Total Accepted: 89221
Total Submissions: 281923
Difficulty: Medium
Contributors: Admin
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
Hide Company Tags Bloomberg
Hide Tags Backtracking
Hide Similar Problems (H) Palindrome Partitioning II

"""


class Solution(object):

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]

        The only tricky part is to understand why we have all the palindrome
        partitions this way, even while not going back when we have a new
        partition. It comes from the properties of a palindrome, which can
        always be grown from its middle (second case in the code) or left to right.
        """
        def partitionRec(p, index, ps):
            # If we're at the last position of the current partition, add the
            # partition and leave.
            if index == len(p) - 1:
                ps += [p]
                return
            # Tries to create a palindrome at "index"
            if p[index] == p[index + 1]:  # first way 'ab', 'ba'
                pi = p[:]
                pi[index] = pi[index] + pi[index + 1]
                del pi[index + 1]
                # go look for other partitions based on the new one
                partitionRec(pi, index, ps)
            if index > 0 and p[
                    index -
                    1] == p[
                    index +
                    1]:  # second way 'ab', 'c', 'ba'
                pii = p[:]
                pii[index - 1] = pii[index - 1] + pii[index] + pii[index + 1]
                del pii[index + 1]
                del pii[index]
                # go look for other partitions based on the new one
                partitionRec(pii, index - 1, ps)
            # Go forward on the ame partition
            partitionRec(p, index + 1, ps)

        def partitionHelper(s):
            p = [c for c in s]  # initialize the first partition
            ps = []  # initialize list of partitions
            partitionRec(p, 0, ps)  # go!
            return ps

        return partitionHelper(s)
