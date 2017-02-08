"""
72. Edit Distance   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 78038
Total Submissions: 254104
Difficulty: Hard
Contributors: Admin
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
Hide Tags Dynamic Programming String
Hide Similar Problems (M) One Edit Distance

"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        match up
        word1
        word2
        dp[i][j] means the minmum points for i numbers of word1[i] matching j numbers of word2[j]
        three possibilities:
        dp[i-1][j-1]+same(word1[i],word2[j])
        dp[i-1][j]+1, dp[i][j-1]+1

        given:
        dp[0][j]=n
        dp[i][0]=m
        """
        m=len(word1)
        n=len(word2)
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                else:
                    dp[i][j]=min(dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1),dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[m][n]

        
