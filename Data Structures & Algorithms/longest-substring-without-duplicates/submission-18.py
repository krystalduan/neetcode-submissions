class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        result = 0
        left = 0

        for i, ch in enumerate(s):
            if ch in seen:
                result = max(result, i - left)
                left = max(left, seen[ch] + 1)   # never move left backwards
            seen[ch] = i

        return max(result, len(s) - left)