class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [amount+1] * (amount+1)
        num_coins[0] = 0

        for i in range(amount+1):
            for c in coins:
                if i >= c:
                    num_coins[i] = min(num_coins[i], 1+num_coins[i-c])
        return num_coins[amount] if num_coins[amount] != amount+1 else -1