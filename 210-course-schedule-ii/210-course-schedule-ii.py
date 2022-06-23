class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        coursesDone = []
        for i in range(len(courses)):
            if courses[i] == 0:
                curCourses.append(i)
        
        while curCourses:
            nxtCourses = []
            tmpCourseDone = []
            for course in curCourses:
                coursesDone.append(course)
                # remove pre req
                for reqFor in preReq[course]:
                    courses[reqFor] -= 1
                    if courses[reqFor] == 0:
                        nxtCourses.append(reqFor)
                        tmpCourseDone.append(reqFor)
            curCourses = nxtCourses
            # coursesDone = coursesDone + tmpCourseDone
        
        return coursesDone if len(coursesDone) == numCourses else []
            
                
                
        