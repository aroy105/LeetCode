import heapq
class Solution:
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
    You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            # We don't need to actually take the square root since we're not asked to return the absolute difference
            # The relative distances will be in order
            d = (x**2) + (y**2)
            pts.append([d, x, y])

        heapq.heapify(pts) 
        res = []
        for i in range(k):
            d, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res