class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:count[c]+=1

        res = 0
        seenOne = False
        for v in count.values():
            if v%2 == 0:
                res+=v
            else:
                seenOne = True
                res+=(v-1)
                
        if seenOne:res+=1
        return res