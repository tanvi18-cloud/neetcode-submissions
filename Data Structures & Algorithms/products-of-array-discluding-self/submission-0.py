class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [1] * len(nums)       # Creates output array initialized with 1
        prefix = 1                     # Stores product of all elements to the left

        for i in range(len(nums)):     # First pass: left to right
            answer[i] = prefix         # Stores product of elements before current index
            prefix *= nums[i]          # Updates prefix by multiplying current number

        suffix = 1                     # Stores product of all elements to the right

        for i in range(len(nums)-1, -1, -1):  # Second pass: right to left -1 -1 -1 becuase range has start at last index, stop before reaching -1 and step - move backwards by 1
            answer[i] *= suffix        # Multiplies stored prefix by suffix
            suffix *= nums[i]          # Updates suffix using current number

        return answer                  # Returns final product array