"""
140. Word Break II Add to List
DescriptionSubmissionsSolutions
Total Accepted: 82389
Total Submissions: 364449
Difficulty: Hard
Contributors: Admin
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

Hide Company Tags Dropbox Google Uber Snapchat Twitter
Hide Tags Dynamic Programming Backtracking
Hide Similar Problems (M) Word Break (H) Concatenated Words

catsanddog
sanddog
dog
hello  dog [u'dog']
hello dog sanddog [u'sand dog']
hello sand dog catsanddog [u'cat sand dog']
anddog
hello dog anddog [u'and dog']
hello and dog catsanddog [u'cat sand dog', u'cats and dog']

"""


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.words = wordDict
        self.table = {'': ['']}
        return self.backtrack(s)

    def backtrack(self, s):
        if s in self.table:
            return self.table[s]
        print s

        sols = []
        for word in self.words:
            if word == s[:len(word)]:
                for sol in self.backtrack(s[len(word):]):
                    sols.append(word + ' ' + sol if sol else word)
                    print 'hello', sol, s, sols

        self.table[s] = sols
        return sols
