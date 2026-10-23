import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]

        dist = [float('inf')] * (n+1)
        dist[k] = 0

        for u,v,w in times:
            graph[u].append((v,w))

        heap = [(0,k)] #effort and node

        while heap:
            effort, node = heapq.heappop(heap)

            for nei,wei in graph[node]:
                new_effort = effort + wei

                if new_effort < dist[nei]:
                    dist[nei] = new_effort
                    heapq.heappush(heap,(new_effort,nei))

        max_ans = max(dist[1:])
        return -1 if max_ans == float('inf') else max_ans



