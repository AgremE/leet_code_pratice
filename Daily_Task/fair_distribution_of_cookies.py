from typing import List
import heapq


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """
        The goal of the algorithm is to find the smallest k subset number that
        have smallest sum
        """
        cookies = sorted(cookies)
        result = []
        heapq.heapify(result)
        while cookies:
            if len(result) < k:
                heapq.heappush(result, cookies.pop())
            else:
                if len(cookies) == 1:
                    last_elem = cookies.pop()
                    _min = heapq.heappop(result)
                    heapq.heappush(result, _min + last_elem)
                    break
                f_min = heapq.heappop(result)
                s_min = heapq.heappop(result)
                n_f_add = cookies.pop(0)
                n_s_add = cookies.pop(0)
                test = abs(((s_min + n_s_add) - (f_min + n_f_add))) - abs(
                    ((s_min + n_f_add) - (f_min + n_s_add))
                )
                if test <= 0:
                    f_min = f_min + n_f_add
                    heapq.heappush(result, f_min)
                    heapq.heappush(result, s_min)
                    cookies.insert(0, n_s_add)
                else:
                    s_min = s_min + n_f_add
                    heapq.heappush(result, f_min)
                    heapq.heappush(result, s_min)
                    cookies.insert(0, n_s_add)
        return heapq.nlargest(1, result)[0]


solution = Solution()
print(solution.distributeCookies(cookies=[6, 1, 3, 2, 2, 4, 1, 2], k=3))
