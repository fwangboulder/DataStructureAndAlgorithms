"""
54. Spiral Matrix   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 86420
Total Submissions: 350282
Difficulty: Medium
Contributors: Admin
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

Hide Company Tags Microsoft Google Uber
Hide Tags Array
Hide Similar Problems (M) Spiral Matrix II

"""
"""
len(res)=m*n
step 1: di=0,dj=1, trasversal first row
step 2: if arrive end of row, di=1,dj=0
step 3: if arrive end of the last column: di=0,dj=-1
...

"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res=[]
        m,n=len(matrix),len(matrix[0])
        i,j,di,dj=0,0,0,1
        for k in xrange(m*n):
            res.append(matrix[i][j])
            matrix[i][j]=''
            if matrix[(i+di)%m][(j+dj)%n]=='':
                di,dj=dj,-di
            i+=di
            j+=dj
        return res
