class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)  # Total number of houses

        if n == 0:  # No houses
            return 0

        if n == 1:  # Only one house
            return nums[0]

        def rob_linear(houses):  # Solve the linear House Robber problem
            memo = {}  # Store previously calculated results
            length = len(houses)

            def dfs(i):  # Maximum money starting from index i
                if i >= length:  # Reached beyond the last house
                    return 0

                if i in memo:  # Already calculated this index
                    return memo[i]

                rob_current = houses[i] + dfs(i + 2)  # Rob current, skip next
                skip = dfs(i + 1)  # Skip current, move to next

                memo[i] = max(rob_current, skip)  # Save the better choice
                return memo[i]

            return dfs(0)  # Start from the first house

        case1 = rob_linear(nums[:-1])  # Exclude last house
        case2 = rob_linear(nums[1:])  # Exclude first house

        return max(case1, case2)  # Return maximum money