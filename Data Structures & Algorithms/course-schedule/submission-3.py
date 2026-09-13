class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # in_degree = [0] * numCourses
        # course_dependency = [[] for i in range(numCourses)]

        # for s,d in prerequisites:
        #     in_degree[d] += 1
        #     course_dependency[s].append(d)

        # q = deque()
        # for n in range(numCourses):
        #     if in_degree[n] == 0:
        #         q.append(n)
        
        # finish = 0
        # while q:
        #     node = q.popleft()
        #     finish += 1

        #     for neighbor in course_dependency[node]:
        #         in_degree[neighbor] -= 1

        #         if in_degree[neighbor] == 0:
        #             q.append(neighbor)
        # return finish == numCourses

        #DFS APPROACH
        map = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            map[course].append(prereq)
        
        current_course = set()

        def dfs(course):
            if course in current_course:
                return False
            if map[course] == []:
                return True
            
            current_course.add(course)
            for prereq in map[course]:
                if not dfs(prereq):
                    return False
            current_course.remove(course)
            map[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
