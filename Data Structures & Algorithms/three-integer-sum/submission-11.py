class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 1. Sort the array to easily skip duplicates and use two pointers
        nums.sort()
        
        for i in range(len(nums) - 2):
            # Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # If the smallest number is greater than 0, three positive numbers can't sum to 0
            if nums[i] > 0:
                break
                
            # 2. Use two pointers for the remaining part of the array
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    left += 1  # Sum is too small, move left pointer to increase it
                else:
                    right -= 1 # Sum is too big, move right pointer to decrease it
                    
        return result