class Solution:
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1. 
    Return true if you can finish all courses. Otherwise, return false.
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # We essentially have to create a graph of all the functions
        # The only way where it is impossible to finish all the courses is if there's a cycle
        # I.e. both courses are pre-reqs for each other, which isn't possible
        # We use DFS and an adjacency list to recursively check if the courses can be completed
        
        # Create blank adjacency list 
        preMap = {i: [] for i in range(numCourses)}
        # Go though each of the prereqs, and populate the adjacency list
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        # Create a set for DFS
        visiting = set()
        
        def dfs(course):
            # If we have already visited the current course previously, we found a cycle
            if course in visiting:
                return False
            # If the course has no prereqs, it can be finished
            if preMap[course] == []:
                return True 
            # At this point, the course must have prereqs. 
            # Add the course to visiting
            visiting.add(course)
            # For each prereq, run dfs, and if at any time any of the prereqs are impossible to complete, return False
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            # At this point, all the prereqs checked out. We can pop it from visiting & set it to True 
            visiting.remove(course)
            preMap[course] = []
            # By setting it to True, if any future class use course as prereq, we can immediately return True instead of rechecking course's prereqs.
            return True
        
        # For each course we have
        for c in range(numCourses):
            # If DFS ever returns false for any course, return False
            if not dfs(c):
                return False
        # All courses have been demonstrated to be successfully completed. Return True
        return True