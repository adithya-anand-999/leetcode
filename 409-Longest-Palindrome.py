class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        for c in s: count[c]+=1

        oddSeen = False
        length = 0 

        for num in count.values():
            if num%2 == 0:
                length+=num
            else:
                oddSeen = True
                length+=(num-1)
        
        return length+1 if oddSeen else length