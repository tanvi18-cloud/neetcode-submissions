class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:
            heapq.heappush(heap, num) #add number to heap

            if len(heap) > k:#if heap has more elements than k elements
                heapq.heappop(heap) #remove the smallest

        return heap[0] #smallest of k largest = kth largest
        