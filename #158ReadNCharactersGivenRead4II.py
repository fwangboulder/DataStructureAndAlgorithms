"""
158. Read N Characters Given Read4 II - Call multiple times Add to List
DescriptionSubmissionsSolutions
Total Accepted: 23147
Total Submissions: 95102
Difficulty: Hard
Contributors: Admin
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.

Hide Company Tags Bloomberg Google Facebook
Hide Tags String
Hide Similar Problems (E) Read N Characters Given Read4

"""
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
from collections import deque
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        "a"
[read(0),read(1),read(2)]
["","a",""]
        """
        idx = 0
        while True:
            buf4 = [""]*4
            l = read4(buf4)
            self.queue.extend(buf4)
            curr = min(len(self.queue), n-idx)
            for i in xrange(curr):
                buf[idx] = self.queue.popleft()
                idx+=1
            if curr == 0:
                break
        return idx

    def __init__(self):
        self.queue = deque()
