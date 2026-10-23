class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        order = []
        while queue:
            node = queue.popleft()

            if node in visited:
                continue

            visited.add(node)
            order.append(node)

            for nei in graph[node]:
                if nei not in visited:
                    indgree[nei] -= 1

                if indgree[nei] == 0:
                    queue.append(nei)

        return order if len(visited) == numCourses else []
        

        