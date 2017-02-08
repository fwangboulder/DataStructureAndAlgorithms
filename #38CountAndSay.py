"""
38. Count and Say   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 116602
Total Submissions: 355840
Difficulty: Easy
Contributors: Admin
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Hide Company Tags Facebook
Hide Tags String
Hide Similar Problems (M) Encode and Decode Strings

"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s='1'
        for i in range(n-1):
            ns=prev=''
            count=0
            for q in s:
                if prev!='' and q!=prev:
                    ns+=str(count)+prev
                    count=1
                else:
                    count+=1
                prev=q
            ns+=str(count)+prev
            s=ns
        return s
        
