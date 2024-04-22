from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # get graph search base
        def generate(cur_step,deadends):
            next_step = {
                "0":["1","9"],
                "1":["2","0"],
                "2":["1","3"],
                "3":["2","4"],
                "4":["3","5"],
                "5":["4","6"],
                "6":["5","7"],
                "7":["6","8"],
                "8":["7","9"],
                "9":["8","0"]
            }
            result = []
            for i in range(len(cur_step)):
                n_s = next_step[cur_step[i]]
                for _s in n_s:
                    result.append(cur_step[:i] + _s + cur_step[i + 1:])
            return [x for x in list(set(result)) if x not in deadends]
        deadends = set(deadends)
        n_v = ["0000"]
        n_v = [x for x in n_v if x not in deadends]
        already_visit = set()
        temp_n_v = []
        count = 0
        while n_v:
            _v = n_v.pop()
            if _v == target:
                return count
            if _v in already_visit:
                if not n_v:
                    n_v = temp_n_v
                    count+=1
                    temp_n_v = []
                continue
            else:
                already_visit.add(_v)
            temp_n_v = temp_n_v + generate(_v,deadends)
            if not n_v:
                n_v = temp_n_v
                count+=1
                temp_n_v = []
        return -1
solution = Solution()

print(solution.openLock(deadends = ["0000","0101","0102","1212","2002"], target = "0202"))