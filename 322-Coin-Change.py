class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #as lists are 0 indexed and our goal is to find the minCoins for amount we have to do amount+1. So index amount will hold the min number of coins for amount. If I made the length just amount then index wise highest index would just be amount-1 as there would be a index 0.
        #So by doing this we have amount for 1-amount, and the +1 is for index 0 
        minCoins = [amount+1] * (amount+1)
        minCoins[0] = 0

#amount 0 (index 0) is taken care of. So we need to start at index 1 and go till index amount. In other words find minCoins for coin amounts of 1 and amount. 
#'i' is the coin amount
        for i in range(1,amount+1):
            for c in coins:
                #make sure the coin itself is less than or equal to the coint amount
                if c <= i:
                    minCoins[i] = min(minCoins[i], 1+minCoins[i-c])
        return -1 if minCoins[amount] == amount+1 else minCoins[amount]