class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        course_dependency = [[] for i in range(numCourses)]

        for s,d in prerequisites:
            in_degree[d] += 1
            course_dependency[s].append(d)

        q = deque()
        for n in range(numCourses):
            if in_degree[n] == 0:
                q.append(n)
        
        finish = 0
        while q:
            node = q.popleft()
            finish += 1

            for neighbor in course_dependency[node]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        return finish == numCourses