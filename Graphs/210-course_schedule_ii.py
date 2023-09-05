class Solution:
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. 
    If it is impossible to finish all courses, return an empty array.
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # We're going to use Topological Sort
        # For each node, we run DFS
        # First, create a dictionary, where for each course, there is an associated list or prereqs.
        prereq = {c: [] for c in range(numCourses)}
        # Populate the dictionary
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        # Create data structures necessary. Output is our answer
        output = []
        # Visit marks nodes we haev already run through, and cycle will be used to detect cycles (wow so true!)
        visit, cycle = set(), set()
        
        def dfs(crs):
            # If a course was already traversed in a cycle, it means we have an illegal prerequisite scheme. 
            if crs in cycle:
                return False
            # If a course was already visited, then there is no need to repeat it again
            if crs in visit:
                return True
            
            # Now, add the course to the current cycle, and run DFS on its prereqs
            # If at any point a cycle is detected, return False
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            # Pop course off the recursion stack
            cycle.remove(crs)
            # We have now visited the course
            visit.add(crs)
            # Add the course to the answer in order (since this is recursive)
            output.append(crs)
            return True # No violations found yet
        
        # Run DFS on all the courses. If a cycle is found, just return an empty list, since no course selection is possible.
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
        