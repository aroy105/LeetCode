from collections import defaultdict 
class DetectSquares:
    """
    You are given a stream of points on the X-Y plane. Design an algorithm that:
        - Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
        - Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point
        form an axis-aligned square with positive area.
    An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.
    """
    # While there is a tricky n^3 solution, where for a point we basically check every other three points that runs through all other points, there is an easier solution which is just O(n)
    # We can run through the list of diagonals, and in O(n) we can check if a square exists i.e. if the two other points exist, since we have a hashmap
    # THIS SOLUTION STILL SEEMS TO BE VERY SLOW AND MEMORY INTENSIVE COMPARED TO OTHERS ON LEETCODE
    def __init__(self):
        """Initializes the object with an empty data structure."""
        # We could use a regular dictionary, but defaultdict makes things easier since it'll always return 0 by default if the key doesn't exist
        # The dictionary structure will be (x, y): # of instances
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        """Adds a new point point = [x, y] to the data structure."""
        self.pts.append(point)
        # We also need to count duplicate points, since this can be used to form another square
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        """Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above."""
        res = 0
        x1, y1 = point
        for x2, y2 in self.pts:
            # We can skip the point if the difference in the x and y directions are not identical (it's a square, so this value should be equal), 
            # or if they share a coordinate in x or y (either a line would be only possible shape formed or we chose a duplicate point)
            if (abs(y1 - y2) != abs(x1 - x2)) or x2 == x1 or y2 == y1:
                continue
            # At this point, we found a diagonal. In O(1), we can check if the other two points exist by using x from one corner and y from the other. 
            # Since there may be duplicate, it's possible that while only 1 variant of one corner exists, there are 3 identical corners for the remaining spot. Thus, 3 squares can be made.
            # Likewise, if 4 duplicate corners exist for one, and 6 for the other, we then can add 4*6 = 24 squares to our running count
            res += self.ptsCount[(x2, y1)] * self.ptsCount[(x1, y2)]
        # After running through all the possible diagonals, return the result
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)