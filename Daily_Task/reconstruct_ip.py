from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ## Maybe that just a constructive algorithm
        def invalide_leading_zero(_str):
            total_sum = sum([int(x) for x in _str])
            if _str[0] != "0":
                if int(_str) > 255:
                    return True
            if total_sum > 0 and _str[0] == "0":
                return True
            elif total_sum == 0 and len(_str) > 1:
                return True
            return False

        len_s = len(s)
        if len_s > 12:
            return []
        result = []
        for i_1 in range(3):
            first_ind = i_1 + 1
            first_part = s[:first_ind]
            if len(first_part) == 0:
                continue
            if invalide_leading_zero(first_part):
                break
            for i_2 in range(3):
                second_ind = first_ind + i_2 + 1
                second_part = s[first_ind:second_ind]
                if len(second_part) == 0:
                    continue
                if invalide_leading_zero(second_part):
                    break
                for i_3 in range(3):
                    third_ind = second_ind + i_3 + 1
                    third_part = s[second_ind:third_ind]
                    if len(third_part) == 0:
                        continue
                    if invalide_leading_zero(third_part):
                        break
                    fouth_part = s[third_ind:]
                    if (len(fouth_part) > 3 == 0) or len(fouth_part) == 0:
                        continue
                    if invalide_leading_zero(fouth_part):
                        continue
                    result.append(
                        f"{first_part}.{second_part}.{third_part}.{fouth_part}"
                    )
        return result


solution = Solution()
print(solution.restoreIpAddresses(s="101023"))
