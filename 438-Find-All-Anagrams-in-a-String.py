class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pl = len(p)
        sl = len(s)
        if sl < pl: return []

        res = []
        freq_p = defaultdict(int)
        window = defaultdict(int)
        for i,c in enumerate(p):
            freq_p[c]+=1
            window[s[i]]+=1
        if window == freq_p: res.append(0)
        for i in range(pl,sl):
            window[s[i]]+=1
            window[s[i-pl]]-=1
            if not window[s[i-pl]]: del window[s[i-pl]]
            if window == freq_p: res.append(i-pl+1)
        return res
