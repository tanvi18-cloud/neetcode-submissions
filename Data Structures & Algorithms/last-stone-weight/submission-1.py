class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        heap = []  # Create an empty heap

        # Convert every stone into a negative number
        for stone in stones:
            heapq.heappush(heap, -stone)

        # Keep smashing stones while at least 2 remain
        while len(heap) > 1:

            # Remove the heaviest stone
            first = -heapq.heappop(heap)

            # Remove the second heaviest stone
            second = -heapq.heappop(heap)

            # If weights are different, calculate the difference
            if first != second:
                difference = first - second

                # Add the remaining stone back into the heap
                heapq.heappush(heap, -difference)

        # If one stone remains, return its weight
        if heap:
            return -heap[0]

        # If no stones remain, return 0
        return 0