from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [[i] for i in range(1,n+1)]
        for _k in range(1,k+1):
            tracker = {}
            temp_result = []
            for _n in range(2,n+1):
                for i in range(len(result)):
                    _list_n = result[i]
                    if i in _list_n:
                        continue
                    _list_n.append(i)
                    _list_n = sorted(_list_n)
                    _id = "".join([str(x) for x in _list_n])
                    if _id in tracker:
                        continue
                    else:
                        tracker[_id] = 1
                        temp_result.append(_list_n)
            result = temp_result.copy()
        return result