class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                #window size if i chars
                #dp[J] checks if first j chars can be made, j<i as its range(i) so never i
                #s[j:i] in wordSet checks if chars after first j inside wordSet.
                #If both true then dp[i] can be made fully.
                    dp[i] = True
                    break
        return dp[n]
