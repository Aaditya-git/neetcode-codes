class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        counter = 0

        for start in range(len(graph)):

            if start in visited:
                continue
            
            stack = [start]

            while stack:

                node = stack.pop()

                if node in visited:
                    continue
                
                visited.add(node)

                for nei in graph[node]:
                    if nei not in visited:
                        stack.append(nei)

            counter += 1

        return counter

                

                


        