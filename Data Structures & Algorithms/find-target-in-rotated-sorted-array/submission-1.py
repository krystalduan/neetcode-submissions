class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return m
            target_high = target > nums[right]
            m_high = nums[m] > nums[right]
            if target_high == m_high:      # same run: ordinary binary search
                if target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            elif target_high:              # target in high run, m in low run
                right = m - 1
            else:                          # target in low run, m in high run
                left = m + 1
        return -1