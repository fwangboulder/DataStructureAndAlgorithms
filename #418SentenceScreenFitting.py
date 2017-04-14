"""
418. Sentence Screen Fitting Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 9833
Total Submissions: 35865
Difficulty: Medium
Contributor: LeetCode
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output:
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
Hide Company Tags Google
Hide Tags Dynamic Programming

"""
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        #the last space is used for refill sentence[0]
        s=" ".join(sentence)+" "
        l=len(s)
        start=0
        for _ in xrange(rows):
            start+=cols-1
            if s[start%l]==" ":
                start+=1
            elif s[(start+1)%l]==" ":
                start+=2
            else:
                while start>0 and s[(start-1)%l]!=" ":
                    start-=1
        return start/l
