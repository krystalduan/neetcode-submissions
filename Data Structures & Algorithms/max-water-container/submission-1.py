class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        # height = 0
        i = 0
        j = len(heights) - 1 
          
        while i < j: 
            width = j - i
            height = min(heights[i], heights[j])
            volume = max(volume, height * width)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return volume
        