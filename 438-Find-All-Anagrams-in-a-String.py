class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pL = len(p)
        sL = len(s)

        if sL<pL: return []


        res = []
        window = defaultdict(int)
        freq_p = defaultdict(int)

        for i,c in enumerate(p): 
            freq_p[c]+=1
            window[s[i]]+=1

        if window == freq_p: res.append(0)
        # would storing the range in a variable be better computatianlly as each time the loop runs it would have to evaluate the expression
        for i in range(pL,sL):
            window[s[i]]+=1
            window[s[i-pL]]-=1
            if window[s[i-pL]]==0: del window[s[i-pL]]
            if window == freq_p: res.append(i-pL+1)

        # i = 0
        # while i<(sL-pL):
        #     if window == freq_p: res.append(i)
        #     window[s[i]]-=1
        #     window[s[i+pL]]+=1
        #     i+=1
        # print(i)
        # if window == freq_p: res.append(i)

        return res