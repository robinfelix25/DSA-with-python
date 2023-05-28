
def numIslands(grid):
    ROW, COL = len(grid), len(grid[0])
    visited = set()
    island = 0
    def dfs(r, c):
        if ((r,c) in visited or
            r < 0 or c < 0 or
            r >= ROW or c >= COL or
            grid[r][c] == "0"):
            return 0

        visited.add((r,c))
        
        # This was expressed in for loop below, Simplicity i made this here
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

        # directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # for dr, dc in directions:
        #     dfs(dr + r, dc + c)
    for r in range(ROW):
        for c in range(COL):
            if ((r,c)) not in visited and grid[r][c] == "1":
                island += 1
                dfs(r,c)
   
    return island

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))