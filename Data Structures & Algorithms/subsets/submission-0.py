class Solution:
    def subsets(self, nums):

        result = []       # Stores ALL the subsets we find
        path = []         # Stores the CURRENT subset we are building

        def backtrack(i): # i tells us which number we are currently considering

            # BASE CASE
            if i == len(nums):          # Have we considered every number?
                result.append(path.copy()) # Save a COPY of the current subset
                return                  # Stop this branch of recursion

            # CHOICE 1: INCLUDE the current number
            path.append(nums[i])        # Add the current number to our subset
            backtrack(i + 1)            # Move to the next number

            # UNDO the choice
            path.pop()                  # Remove the number we just added

            # CHOICE 2: EXCLUDE the current number
            backtrack(i + 1)            # Move to the next number without adding it

        backtrack(0)                    # Start from index 0 (first number)

        return result                   # Return all the subsets