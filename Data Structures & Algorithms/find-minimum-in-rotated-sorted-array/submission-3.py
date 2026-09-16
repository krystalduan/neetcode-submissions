class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = 1000
        while left <= right:
            m = int((left + right) / 2)
            result = min(nums[m], result)
            if nums[m] >= nums[right]:
                left = m + 1
            else: 
                right = m - 1
        return result



        
        
        