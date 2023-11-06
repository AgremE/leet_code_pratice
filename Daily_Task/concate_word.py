from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        start_w = {}
        for word in words:
            s_c = word[0]
            if s_c in start_w:
                start_w[s_c].append((word, len(word)))
            else:
                start_w[s_c] = [(word, len(word))]

        def find_concated_sub_string(_input, start_w, avoid_compare=""):
            if _input == "":
                return 1
            _s_c = _input[0]
            if not (_s_c in start_w):
                return 0
            s_w_list = start_w[_s_c]
            result = [0]
            for _w_info in s_w_list:
                _w, _l = _w_info
                if _w == avoid_compare:
                    continue
                if _w == _input[:_l]:
                    result.append(
                        find_concated_sub_string(_input[_l:], start_w, avoid_compare)
                    )
            return sum(result) >= 1

        result = []
        for word in words:
            if find_concated_sub_string(word, start_w, word) == 1:
                result.append(word)
        return result


solution = Solution()
print(
    solution.findAllConcatenatedWordsInADict(
        words=[
            "cat",
            "cats",
            "catsdogcats",
            "dog",
            "dogcatsdog",
            "hippopotamuses",
            "rat",
            "ratcatdogcat",
        ]
    )
)

print(solution.findAllConcatenatedWordsInADict(words=["cat", "dog", "catdog"]))
