class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]       # Best subarray sum ending here
        maximum = nums[0]       # Best sum found overall

        for num in nums[1:]:    # Visit remaining elements

        # Start fresh OR extend the previous subarray
          current = max(num, current + num)

        # Update the overall maximum
          maximum = max(maximum, current)

        return maximum      
        