class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r_len = len(grid)
        c_len = len(grid[0])

        directions = [(-1,0),(1,0),(0,-1),(0,1)] #specifies where you wanna move 

        stack = []
        visited = set()
        island = 0

        for r in range(r_len):
            for c in range(c_len):
                if grid[r][c] == '1' and (r,c) not in visited:
                    island += 1
                    visited.add((r,c))
                    stack.append((r,c))

                while stack:
                    curr_r,curr_c = stack.pop()

                    for dr, dc in directions:
                        nr = curr_r + dr
                        nc = curr_c + dc

                        if 0<=nr<r_len and 0<=nc<c_len and (nr,nc) not in visited:
                            if grid[nr][nc]=='1':
                                visited.add((nr,nc))
                                stack.append((nr,nc))
        return island








