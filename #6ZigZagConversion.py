"""
6. ZigZag Conversion   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 132155
Total Submissions: 508971
Difficulty: Easy
Contributors: Admin
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
Hide Tags String
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or len(s)<=numRows:
            return s
        res=['']*numRows
        index,step=0,1
        for i in s:
            res[index]+=i
            if index==0:
                step=1          #increasing 
            elif index==numRows-1:
                step=-1         #decreasing
            index+=step
        return ''.join(res)
