class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        memo = {}

        def dfs(i):
            if i>=n:
                return 0

            if i in memo:
                return memo[i]
            
            rob_current = nums[i] + dfs(i+2)
            skip = dfs(i+1)

            memo[i] = max(rob_current, skip)

            return memo[i]
        return dfs(0)
        