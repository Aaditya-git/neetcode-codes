class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        stack = [(0,-1)]

        while stack:
            node, parent = stack.pop()

            if node in visited:
                return False

            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                
                if nei in visited:
                    return False
                
                stack.append((nei,node))

        return len(visited) == n




        