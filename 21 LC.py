class Solution(object):
    def uniquePaths(self, m, n):
        ans = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0:
                    ans[i][j] = 1
                elif j==0:
                    ans[i][j] = 1
                else: 
                    ans[i][j] = ans[i][j-1] + ans[i-1][j]        
        return ans[m-1][n-1]
