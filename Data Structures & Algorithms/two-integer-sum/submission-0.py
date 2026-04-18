class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement_dict = {}

        for index,num in enumerate(nums):

            subtraction = target - nums[index]

            if subtraction in complement_dict:
                return [complement_dict[subtraction],index]
            else:
                complement_dict[num] = index
            
        return []


        