class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_val = 0

        left = 0
        right = len(heights) - 1 

        while left < right:
            if heights[left] < heights[right]:
                area = heights[left] * (right - left)
                left += 1
            else:
                area = heights[right] * (right - left)
                right -= 1
            max_val = max(max_val,area)
        return max_val
        
    
    # 1,7,2,5,4,7,3,6
    #   l           r
    # max_val = 7