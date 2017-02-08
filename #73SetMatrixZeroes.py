"""
73. Set Matrix Zeroes   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 90422
Total Submissions: 256783
Difficulty: Medium
Contributors: Admin
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Hide Company Tags Microsoft Amazon
Hide Tags Array
Hide Similar Problems (M) Game of Life

"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if not matrix:
            return matrix
        m=len(matrix)
        n=len(matrix[0])
        if n==0:
            return matrix
        i=0
        row=set()
        col=set()
        while i<m:
            j=0
            while j<n:
                #print m,n,i,j,matrix[i][j]
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)

                j+=1
            i+=1
        print row, col
        for i in row:
            for j in range(n):
                matrix[i][j]=0
        for j in col:
            for i in range(m):
                matrix[i][j]=0

                
