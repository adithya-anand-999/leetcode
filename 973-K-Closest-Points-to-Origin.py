import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x,y in points:
            heapq.heappush(min_heap, (-math.sqrt(x**2 + y**2), (x,y)))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [points for (_,points) in min_heap]