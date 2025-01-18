class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [amount+1]*(amount+1)
        num_coins[0] = 0

        for i in range(1,amount+1):
            for c in coins:
                if c<=i:
                    num_coins[i] = min(1+num_coins[i-c],num_coins[i])
        return num_coins[amount] if num_coins[amount]!=amount+1 else -1