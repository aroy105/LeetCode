class DetectSquares:
    """
    You are given a stream of points on the X-Y plane. Design an algorithm that:
        - Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
        - Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point
        form an axis-aligned square with positive area.
    An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.
    """
    def __init__(self):
        """Initializes the object with an empty data structure."""
        pass

    def add(self, point: List[int]) -> None:
        """Adds a new point point = [x, y] to the data structure."""
        pass

    def count(self, point: List[int]) -> int:
        """Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above."""
        pass


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)