class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        r_len = len(grid)
        c_len = len(grid[0])
        INF = 2147483647

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        stack = deque()

        for r in range(r_len):
            for c in range(c_len):
                if grid[r][c]==0:
                    stack.append((r,c))

        while stack:
            curr_r,curr_c = stack.popleft()

            for dr,dc in directions:
                nr = dr + curr_r
                nc = dc + curr_c

                if 0<=nc<c_len and 0<= nr<r_len and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[curr_r][curr_c] + 1
                    stack.append((nr,nc))

            

        