class Solution:
    def frequencySort(self, s: str) -> str:
        dict_count = {}
        for _s in s:
            if _s in dict_count:
                dict_count[_s] = dict_count[_s] + 1
            else:
                dict_count[_s] = 1
        values = list(dict_count.values())
        keys = list(dict_count.keys())
        list_count = [(x[0], x[1]) for x in zip(keys, values)]
        sorted_list = sorted(list_count, key=lambda t: t[1], reverse=True)
        result = ""
        for elem in sorted_list:
            result = result + elem[1] * elem[0]
        return result


solution = Solution()
print(solution.frequencySort("tree"))
print(solution.frequencySort("cccaaa"))
