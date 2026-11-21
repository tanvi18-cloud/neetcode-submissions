class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = nums[0]  # Best sum ending at current position
        max_sum = nums[0]      # Best sum found so far

        for i in range(1, len(nums)):

            num = nums[i]

            # Either start fresh or extend previous subarray
            current_sum = max(num, current_sum + num)

            # Update the maximum sum
            max_sum = max(max_sum, current_sum)

        return max_sum