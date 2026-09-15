class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count.keys():
                count[num] += 1
            else: 
                count[num] = 1
        
        freq = [[] for i in range(len(nums) + 1)]
        for key, value in count.items(): 
            freq[value].append(key)

        result = []
        for value in reversed(freq):
            for num in value:
                result.append(num)
                if len(result) == k:
                    return result