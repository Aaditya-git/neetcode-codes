from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]
        indgree = [0] * numCourses

        for course,mand_course in prerequisites:
            graph[mand_course].append(course)
            indgree[course] += 1
        
        queue = deque()
        visited = set()
        for idx in range(len(indgree)):
            if indgree[idx] == 0:
                queue.append(idx)
        
        while queue:
            node = queue.popleft()

            if node in visited:
                continue

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    indgree[nei] -= 1

                if indgree[nei] == 0:
                    queue.append(nei)
                
        return True if len(visited) == numCourses else False
        

        