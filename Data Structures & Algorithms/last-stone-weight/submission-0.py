class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        
        heap = []

    # Convert stones into negative values
        for stone in stones:
            heapq.heappush(heap, -stone)

    # Continue until at most one stone remains
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

        # If weights are different, push their difference
            if first != second:
                difference = first - second
                heapq.heappush(heap, -difference)

    # Return remaining stone, or 0 if none remain
        if heap:
            return -heap[0]

        return 0
        