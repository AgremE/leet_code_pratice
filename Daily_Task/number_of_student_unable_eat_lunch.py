from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while sandwiches:
            sanwich = sandwiches.pop(0)
            set_student = set(students)
            if (len(set_student) == 1):
                if sanwich != students[0]:
                    break
            if sanwich == students[0]:
                students.pop(0)
            else:
                move_s = students.pop(0)
                students.append(move_s)
                sandwiches.insert(0,sanwich)
        return len(students)

solution = Solution()
print(solution.countStudents(students =
[1,1,0,0],sandwiches =
[0,1,0,1]))