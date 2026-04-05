class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for num in range(len(nums)):
            nums[num] *= nums[num]
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res.append(nums[right])
                right = right - 1
            else:
                res.append(nums[left])
                left = left + 1
        return res[::-1]
        