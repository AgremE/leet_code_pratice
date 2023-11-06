from pydoc import plainpager
from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plantGrowTime = {}
        temp_plant_time = plantTime.copy()
        plantTime = growTime.copy()
        growTime = temp_plant_time.copy()
        for i in range(len(plantTime)):
            _time = plantTime[i]
            if _time in plantGrowTime:
                plantGrowTime[_time].append(growTime[i])
            else:
                plantGrowTime[_time] = [growTime[i]]
        for key, value in plantGrowTime.items():
            value.sort(reverse=True)
            plantGrowTime[key] = value
        max_time = 0
        reminding_grow_time = 0
        previous_plant_time = 0
        ### Construct a max time for each cluster and reminding grow
        max_remind_grow = {}
        sort_plant_time = list(set(plantTime))
        sort_plant_time.sort(reverse=True)
        for _x in sort_plant_time:
            key = _x
            value = plantGrowTime[key]
            for i in range(len(value)):
                _val = value[i]
                total_plant_time = key + (i + 1) * _val + previous_plant_time
                if max_time <= total_plant_time:
                    max_time = total_plant_time
                    reminding_grow_time = _val
                else:
                    reminding_grow_time = max_time - (_val + (i + 1) * key)
            previous_plant_time = previous_plant_time + sum(value)
        return max_time


solution = Solution()
print(solution.earliestFullBloom([1, 4, 3], [2, 3, 1]))
print(solution.earliestFullBloom([1, 2, 3, 2], [2, 1, 2, 1]))
print(solution.earliestFullBloom([1], [1]))
