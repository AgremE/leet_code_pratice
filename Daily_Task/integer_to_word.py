class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        thousand_split = ["", "Thousand", "Million", "Billion"]
        sub_twenty = {
            19: "Nineteen",
            18: "Eighteen",
            17: "Seventeen",
            16: "Sixteen",
            15: "Fifteen",
            14: "Fourteen",
            13: "Thirteen",
            12: "Twelve",
            11: "Eleven",
            10: "Ten",
        }
        one_digit = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }
        teent_digit = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }

        def get_sub_thousand_split(num, ext=""):
            # Assuming the input at 999 -> convert to english with sub 1000
            hundre = num // 100
            last_two_digit = num % 100
            if num == 0:
                return ""
            if last_two_digit < 10:
                if hundre != 0:
                    return f"""{one_digit[hundre]} Hundred {one_digit.get(last_two_digit,"")}""".strip()
                else:
                    return f"{one_digit[last_two_digit]}".strip()
            words = sub_twenty.get(last_two_digit, None)
            if words:
                if hundre != 0:
                    return f"{one_digit[hundre]} Hundred {words}".strip()
                else:
                    return words
            else:
                teent_num = last_two_digit // 10
                last_digit = last_two_digit % 10

                last_two_words = f"""{teent_digit.get(teent_num,"")} {one_digit.get(last_digit,"")}""".strip()
                if hundre != 0:
                    if last_two_words != "":
                        return f"{one_digit[hundre]} Hundred {last_two_words}".strip()
                    else:
                        return f"{one_digit[hundre]} Hundred".strip()
                else:
                    return last_two_words.strip()

        result = []
        while num:
            temp_num = num % 1000
            num = num // 1000
            partial_string = get_sub_thousand_split(temp_num)
            result.append(partial_string)
        result = result
        for i in range(len(result)):
            if result[i] == "":
                continue
            result[i] = result[i] + f" {thousand_split[i]}"
        return " ".join([x for x in result[::-1] if x != ""]).strip()


solution = Solution()
print(solution.numberToWords(1000010))
