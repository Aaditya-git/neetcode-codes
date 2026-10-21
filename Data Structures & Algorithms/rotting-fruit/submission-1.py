from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r_len = len(grid)
        c_len = len(grid[0])
        visited = set()
        queue = deque()
        fresh = 0
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        for r in range(r_len):
            for c in range(c_len):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1

        minutes = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                curr_r,curr_c = queue.popleft()

                for dr ,dc in directions:
                    nr = curr_r + dr
                    nc = curr_c + dc 

                    if 0<=nr<r_len and 0<=nc<c_len:
                        if grid[nr][nc] == 1 and (nr,nc) not in visited:
                            visited.add((nr,nc))
                            fresh -= 1
                            queue.append((nr,nc))
                            # grid[nr][nc] = 2
            minutes += 1
        return minutes if fresh==0 else -1

                


        