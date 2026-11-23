class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}  
        # Create an empty dictionary (hash map).
        # It stores numbers as keys and their indices as values.
        # Example: {2: 0, 7: 1}

        for i in range(len(nums)):
            # Loop through the array using indices.
            # i represents the current index (0, 1, 2, ...).

            complement = target - nums[i]
            # Calculate the number we need to reach the target.
            # Example: target = 9, nums[i] = 2
            # complement = 9 - 2 = 7

            if complement in seen:
                # Check whether the required number already exists
                # in our dictionary.

                return [seen[complement], i]
                # If found, return:
                # 1. Index of the complement (from dictionary).
                # 2. Index of the current number (i).

            seen[nums[i]] = i
            # If complement wasn't found, store the current number
            # and its index in the dictionary.
            # Example: if nums[i] = 2 and i = 0
            # seen becomes {2: 0}