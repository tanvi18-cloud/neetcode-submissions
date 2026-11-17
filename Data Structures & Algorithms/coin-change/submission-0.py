class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remaining):
            if remaining == 0:
                return 0

            if remaining < 0:
                return -1

            if remaining in memo:
                return memo[remaining]

            minimum = float("inf")

            for coin in coins:
                result = dfs(remaining - coin)

                if result != -1:
                    candidate = 1 + result
                    minimum = min(minimum, candidate)

            memo[remaining] = minimum

            return -1 if minimum == float("inf") else minimum

        return dfs(amount)