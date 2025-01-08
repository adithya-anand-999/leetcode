class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        max_len = 0

        for c in s:
            while c in window:
                window.remove(s[l])
                l+=1
            window.add(c)
            max_len = max(max_len, len(window))

        return max_len