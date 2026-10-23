class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        r_len = len(grid)
        c_len = len(grid[0])

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        stack = []
        visited = set()

        max_area = 0

        for r in range(r_len):
            for c in range(c_len):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = 0
                    visited.add((r,c))
                    stack.append((r,c))
                
                    while stack:
                        curr_r, curr_c = stack.pop()
                        area +=1
                        for dr, dc in directions:
                            nr = dr + curr_r
                            nc = dc + curr_c

                            if 0 <=nr<r_len and 0<=nc< c_len and (nr,nc) not in visited:
                                if grid[nr][nc] == 1:
                                    visited.add((nr,nc))
                                    stack.append((nr,nc))
                                
                    max_area = max(max_area,area)

        return max_area









        