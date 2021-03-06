"""
30. Substring with Concatenation of All Words   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 71444
Total Submissions: 329020
Difficulty: Hard
Contributors: Admin
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
Hide Tags Hash Table Two Pointers String
Hide Similar Problems (H) Minimum Window Substring
"""


class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]

        travel all the words combinations to maintain a window
        there are wl(word len) times travel
        each time, n/wl words, mostly 2 times travel for each word
        one left side of the window, the other right side of the window
        so, time complexity O(wl * 2 * N/wl) = O(2N)
        """

        result = []
        if not words or len(s) < len(words) * len(words[0]):
            return result
        wl, count, n, word_dict = len(words[0]), len(words), len(s), {}
        # init word occurence
        for w in words:
            word_dict[w] = word_dict.get(w, 0) + 1
        # travel all sub string combinations
        for i in range(wl):
            start, cnt, tmp_dict = i, 0, {}
            for j in range(i, n - wl + 1, wl):
                str = s[j: j + wl]
                # a valid word, accumulate results
                if word_dict.get(str):
                    cnt += 1
                    tmp_dict[str] = tmp_dict.get(str, 0) + 1
                    # a more word, advance the window left side possiablly
                    while tmp_dict[str] > word_dict[str]:
                        tmp_dict[s[start: start + wl]] -= 1
                        start += wl
                        cnt -= 1
                    # come to a result
                    if cnt == count:
                        result.append(start)
                        # advance one word
                        tmp_dict[s[start: start + wl]] -= 1
                        start += wl
                        cnt -= 1
                # not a valid word, reset all vars
                else:
                    start, cnt, tmp_dict = j + wl, 0, {}
        return result
