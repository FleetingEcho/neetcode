class Solution:
    def climbStairs(self, n: int) -> int:
        base=[1,1,2]
        if n<=2:
            return base[n]
        dp=[0]*(n+1)
        dp[0],dp[1],dp[2]=1,1,2
        for i in range(3,n+1):
            dp[i]=dp[i-2]+dp[i-1]
        return dp[n]

#只能跳1 or 2步