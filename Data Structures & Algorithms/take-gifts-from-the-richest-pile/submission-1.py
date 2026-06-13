import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
      
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        total = sum(gifts)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            remaining = math.isqrt(largest)  

            total = total - largest + remaining

            heapq.heappush(max_heap, -remaining)

        return total