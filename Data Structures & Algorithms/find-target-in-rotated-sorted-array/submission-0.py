class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0                          # Start of the array
        right = len(nums) - 1             # End of the array

        while left <= right:              # Continue while elements remain
            mid = (left + right) // 2     # Find the middle index

            if nums[mid] == target:       # If middle value is our target
                return mid                # Return its original index

            if nums[left] <= nums[mid]:   # Check if the LEFT half is sorted

                if nums[left] <= target < nums[mid]:
                    right = mid - 1       # Target is in left half, search left
                else:
                    left = mid + 1        # Target is in right half, search right

            else:                         # Otherwise, RIGHT half is sorted

                if nums[mid] < target <= nums[right]:
                    left = mid + 1        # Target is in right half, search right
                else:
                    right = mid - 1       # Target is in left half, search left

        return -1                         # Target was not found