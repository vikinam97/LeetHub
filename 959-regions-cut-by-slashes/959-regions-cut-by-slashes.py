class Solution:
    

    def regionsBySlashes(self, grid):
        n, dict1 = len(grid), {}

        def find(x):
            if x not in dict1:
                return x
            else:
                return find(dict1[x])

        def union(x,y):
            parent_x, parent_y = find(x), find(y)

            if parent_x != parent_y:
                dict1[parent_y] = parent_x


        for i in range(n):
            for j in range(n):
                if i>0: union((i-1,j,2), (i,j,0))
                if j>0: union((i,j-1,1), (i,j,3))

                if grid[i][j] != "/":
                    union((i,j,0), (i,j,1))
                    union((i,j,2), (i,j,3))

                if grid[i][j] != "\\":
                    union((i,j,0), (i,j,3))
                    union((i,j,1), (i,j,2))


        return len({find(i) for i in dict1})