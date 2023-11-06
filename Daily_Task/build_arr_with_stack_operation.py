from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        first_tar = target[0]
        init_list = []
        if first_tar > 1:
            init_list.extend(["Push" for _ in range(first_tar - 1)])
            init_list.extend(["Pop" for _ in range(first_tar - 1)])
            init_list.append("Push")
        else:
            init_list = ["Push"]
        for i in range(1, len(target)):
            len_push_pop = target[i] - target[i - 1] - 1
            if len_push_pop > 0:
                init_list.extend(["Push" for _ in range(len_push_pop)])
                init_list.extend(["Pop" for _ in range(len_push_pop)])
                init_list.append("Push")
            else:
                init_list = init_list.append("Push")
        return init_list


solution = Solution()
print(solution.buildArray(target=[1, 4], n=4))
