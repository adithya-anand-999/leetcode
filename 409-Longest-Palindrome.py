class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)
        for c in s: 
            freq[c]+=1
        
        add_one = False
        res = 0
        for val in freq.values():
            if val%2 == 0:
                res += val
            else: 
                add_one = True
                res+=(val-1)
        if add_one: res+=1
        return res        