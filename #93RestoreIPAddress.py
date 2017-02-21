"""
93. Restore IP Addresses Add to List
Description  Submission  Solutions
Total Accepted: 76437
Total Submissions: 292453
Difficulty: Medium
Contributors: Admin
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

Hide Tags Backtracking String

"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result=[]
        index=0
        depth=0
        path=[]
        self.dfs(result,s,path,index,depth)
        return result
    def dfs(self,result,s,path,index,depth):
        if depth==4 and index==len(s):
            result.append('.'.join(path))
        if depth>=4 or index>=len(s):
            return
        else:
            for i in range(index, max(index+3,len(s))):
                t=s[index:i+1]
                if t[0]=='0' and t!='0':
                    continue
                if 255>=int(t)>=0:
                    self.dfs(result,s,path+[t],i+1, depth+1)
