class Solution:
    def combinationSum(self, candidates, target):

        result = []       # Stores all valid combinations
        path = []         # Stores the combination we are currently building

        candidates.sort() # Sort numbers so we can stop early when they exceed target

        def backtrack(i, total):

            # BASE CASE: We found a combination equal to target
            if total == target:
                result.append(path.copy())  # Save a copy of this valid combination
                return                      # Stop exploring this branch

            # Try choosing each candidate, starting from index i
            for j in range(i, len(candidates)):

                # If adding this number exceeds target, larger numbers won't work either
                if candidates[j] > target - total:
                    break

                path.append(candidates[j])  # Choose this number

                # Use j again because the same number CAN be reused
                backtrack(j, total + candidates[j])

                path.pop()                  # Undo the choice and try another candidate

        backtrack(0, 0)                     # Start at index 0 with total 0

        return result                       # Return all valid combinations