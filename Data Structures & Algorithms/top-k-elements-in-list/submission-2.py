class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = {}
        heap = []
        res = []
        for num in nums:
            if num not in freq_counter:
                freq_counter[num] = 1
            else:
                freq_counter[num] += 1

        for item in freq_counter:
            heapq.heappush(heap,(-freq_counter[item],item))

        # print(heap)

        while heap and k > 0:
            max_val,freq = heapq.heappop(heap)
            # max_val = -max_val

            res.append(freq)
            k = k-1


        return res