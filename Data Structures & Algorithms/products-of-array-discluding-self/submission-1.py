class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [0] * len(nums)
        right_arr = [0] * len(nums)
        
        left_mult = 1
        right_mult = 1

        for i in range(len(nums)):
            j = -i-1

            left_arr[i] = left_mult
            right_arr[j] = right_mult

            left_mult *= nums[i]
            right_mult *= nums[j]
        
        res = []
        for u,v in zip(right_arr,left_arr):
            res.append(u*v)
        return res