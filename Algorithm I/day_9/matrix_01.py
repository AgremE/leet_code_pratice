from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        def scan(mat: List[List[int]], pos: List[int], memoir: dict, already_visit: List[str]) -> int:
            elem = f"{pos[0]}_{pos[1]}"
            if elem in memoir:
                return memoir[elem]
            if elem in already_visit:
                return 10**9
            if pos[0] < 0 or pos[0] >= m or pos[1] < 0 or pos[1] >= n:
                return 10**9
            if mat[pos[0]][pos[1]] == 0:
                return 0
            else:
                go_left = [pos[0]-1,pos[1]]
                go_right = [pos[0]+1,pos[1]]
                go_up = [pos[0],pos[1]+1]
                go_down = [pos[0],pos[1]-1]
                result = min([1+scan(mat,go_left,memoir,already_visit+[elem]),
                            1+scan(mat,go_right,memoir,already_visit+[elem]),
                            1+scan(mat,go_up,memoir,already_visit+[elem]),
                            1+scan(mat,go_down,memoir,already_visit+[elem])])
                memoir[elem] = result
                return result
        already_visit = []
        memoir = {}
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                mat[i][j] = scan(mat,[i,j],memoir,already_visit)
        return mat

test_solution = Solution()
#print(test_solution.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(test_solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))