from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = []
        list_num = []
        for _d in digits:
            list_num.append(dictionary[_d])
        list_num = list_num[::-1]
        for _list in list_num:
            _temp = []
            if result:
                for _x in result:
                    for _aph in _list:
                        _temp.append(_aph + _x)
                result = _temp
            else:
                result = _list
        return result


solution = Solution()
print(solution.letterCombinations(digits="2"))
