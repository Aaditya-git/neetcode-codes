class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left_arr = [0] * len(nums)
        right_arr = [0] * len(nums)
        left_multiplier = 1
        right_multiplier = 1
        
        for i in range(len(nums)):
            j = -i-1

            left_arr[i] = left_multiplier
            right_arr[j] = right_multiplier 

            left_multiplier = left_multiplier * nums[i]
            right_multiplier =right_multiplier * nums[j]
        
        for l,r in zip(left_arr,right_arr):
            res.append(l*r)
        return res
        

