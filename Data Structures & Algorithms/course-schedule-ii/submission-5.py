class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            map[course].append(prereq)
        result = []
        visited_course, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited_course:
                return True
            
            cycle.add(course)
            for prereq in map[course]:
                if dfs(prereq) == False:
                    return False

            cycle.remove(course)
            visited_course.add(course)
            result.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return result
