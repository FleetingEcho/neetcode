class Solution:
    def numIslands(self,grid) -> int:
        maxRow=len(grid)
        maxCol=len(grid[0])
        res=0

        directions=[(-1,0),(0,-1),(0,1),(1,0)]
        def dfs(i,j):
            if i<0 or i>=maxRow or j<0 or j>=maxCol:
                return
            if grid[i][j] is not '1':
                return
            grid[i][j]='2'

            for dir in directions:
                dfs(i+dir[0],j+dir[1])

        for i in range(maxRow):
            for j in range(maxCol):
                if grid[i][j] is'1':  # if found island
                    dfs(i,j)
                    res+=1
        return res