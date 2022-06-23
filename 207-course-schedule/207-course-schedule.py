class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Solution Topological BFS
        # Time O(N)
        # Space O(N)
        preReq = defaultdict(list)
        courses = [0] * numCourses
        
        for course, req in prerequisites:
            courses[course] += 1
            if req not in preReq:
                preReq[req] = []
            preReq[req].append(course) 
            
        curCourses = []
        for i in range(len(courses)):
            if courses[i] == 0:
                curCourses.append(i)
        
        coursesDone = 0
        while curCourses:
            nxtCourses = []
            for course in curCourses:
                coursesDone += 1
                # remove pre req
                for reqFor in preReq[course]:
                    courses[reqFor] -= 1
                    if courses[reqFor] == 0:
                        nxtCourses.append(reqFor)
                        
            curCourses = nxtCourses
        
        return coursesDone == numCourses
            
                
                
        