class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count_list = [0 for i in range(len(s))]
        first_zero = True
        ind = 0
        count_zero = True
        list_ind = []
        for _c in s:
            if _c == "0" and first_zero:
                continue
            else:
                first_zero = False
                if _c == "0":
                    if count_zero:
                        count_list[ind] = count_list[ind] + 1
                    else:
                        ind = ind + 1
                        list_ind.append(ind)
                        count_list[ind] = 1
                        count_zero = True
                if _c == "1":
                    if count_zero:
                        ind = ind + 1
                        list_ind.append(ind)
                        count_list[ind] = 1
                        count_zero = False
                    else:
                        count_list[ind] = count_list[ind] + 1
        count_list = count_list[min(list_ind) : max(list_ind) + 1]
        last_one = True if s[-1] == "1" else False
        first_zero = True if s[0] == "0" else False
        if last_one:
            count_list = count_list[:-1]
        number_pair = len(count_list) // 2
        count_cost_covert_to_one = []
        total_cost_covert_to_one = 0
        for i in range(number_pair):
            cost_one_ind = 2 * i + 1
            total_cost_covert_to_one = (
                total_cost_covert_to_one + count_list[cost_one_ind]
            )
        count_cost_covert_to_one.append(total_cost_covert_to_one)
        for i in range(number_pair - 1):
            cost_one_ind = 2 * i + 1
            count_cost_covert_to_one.append(
                total_cost_covert_to_one - count_list[cost_one_ind]
            )
            total_cost_covert_to_one = (
                total_cost_covert_to_one - count_list[cost_one_ind]
            )

        ### Sum min of conversion
        total_cost = 0
        for i in range(number_pair):
            if count_list[2 * i] <= count_list[2 * i + 1]:
                total_cost = count_list[2 * i] + total_cost
            else:
                if count_list[2 * i] > count_cost_covert_to_one[i]:
                    total_cost = total_cost + count_cost_covert_to_one[i]
                    break
                else:
                    total_cost = count_list[2 * i] + total_cost
        return total_cost


solution = Solution()
print(solution.minFlipsMonoIncr(s="10011111110010111011"))
print(solution.minFlipsMonoIncr(s="00110"))
print(solution.minFlipsMonoIncr(s="010110"))
print(solution.minFlipsMonoIncr(s="00011000"))
