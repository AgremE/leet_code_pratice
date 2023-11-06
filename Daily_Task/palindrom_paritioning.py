from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]

        def generate_all_palindrom(s):
            result = []
            for i in range(len(s)):
                test_str = s[: i + 1]
                if isPalindrome(test_str):
                    result.append(test_str)
            return result

        result = []
        for i in range(len(s)):
            result.append(generate_all_palindrom(s[i:]))
        result_final = []

        def genereate_par_subseq(
            result_par_list, curr_list=[], curr_ind=0, temp_result=[]
        ):
            if curr_ind >= len(s):
                return curr_list
            for palin in result_par_list:
                next_ind = curr_ind + len(palin)
                if next_ind >= len(s):
                    curr_list.append(palin)
                    temp_result.append(curr_list)
                    continue
                next_result_par_list = result[next_ind]
                curr_list_copy = curr_list.copy()
                curr_list_copy.append(palin)
                genereate_par_subseq(
                    next_result_par_list,
                    curr_list_copy.copy(),
                    next_ind,
                    temp_result,
                )
            return temp_result

        result_final = genereate_par_subseq(result[0])

        return result_final


solution = Solution()
print(solution.partition(s="a"))
