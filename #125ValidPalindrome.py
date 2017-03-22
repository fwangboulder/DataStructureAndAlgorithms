"""
125. Valid Palindrome Add to List
DescriptionSubmissionsSolutions
Total Accepted: 149010
Total Submissions: 579250
Difficulty: Easy
Contributors: Admin
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Hide Company Tags Microsoft Uber Facebook Zenefits
Hide Tags Two Pointers String
Hide Similar Problems (E) Palindrome Linked List

"""


class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # two pointer, one from the start, the other from the end
        # check whether it is a number of a character
        if s is None:
            return False
        if len(s) == 0:
            return True
        start = 0
        end = len(s) - 1
        s = s.lower()
        while start < end:
            if self.isValid(s[start]) and self.isValid(s[end]):
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            elif not self.isValid(s[start]) and self.isValid(s[end]):
                start += 1
            elif self.isValid(s[start]) and not self.isValid(s[end]):
                end -= 1
            else:
                start += 1
                end -= 1
        return True

    def isValid(self, x):
        if x >= 'a' and x <= 'z':
            return True
        elif x >= '0' and x <= '9':
            return True
        else:
            return False
