class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r_len = len(heights)
        c_len = len(heights[0])
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)] #specifies where we want to move
        stack = []
        for c in range(c_len):
            stack.append((0,c))

        for r in range(r_len):
            stack.append((r,0))
        pacific = set()
        while stack:
            curr_r,curr_c = stack.pop()

            if (curr_r,curr_c) in pacific:
                continue
            pacific.add((curr_r,curr_c))

            for dr,dc in directions:
                nr = dr + curr_r
                nc = dc + curr_c

                if 0<=nr<r_len and 0<=nc<c_len and (nr,nc) not in pacific:
                    if heights[nr][nc] >= heights[curr_r][curr_c]:
                        stack.append((nr,nc))

        
        ####################### Atlantic ##############################
        stack = []

        for c in range(c_len):
            stack.append((r_len-1,c))

        for r in range(r_len):
            stack.append((r,c_len-1))
        
        atlantic = set()

        while stack:
            curr_r, curr_c = stack.pop()

            if (curr_r,curr_c) in atlantic:
                continue

            atlantic.add((curr_r,curr_c))

            for dr,dc in directions:
                nr = dr + curr_r
                nc = dc + curr_c

                if 0<=nr<r_len and 0<=nc<c_len and (nr,nc) not in atlantic:
                    if heights[nr][nc] >= heights[curr_r][curr_c]:
                        stack.append((nr,nc))


        res = pacific.intersection(atlantic)

        result = []
        for r, c in res:
            result.append([r, c])

        return result




        