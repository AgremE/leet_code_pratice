class Solution:
    def intToRoman(self, num: int) -> str:
        num_dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        special_case = {
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
        }
        thousand = int(num / 1000)
        hundre = int((num % 1000) / 100)
        ten = int((num % 100) / 10)
        digit = int(num % 10)
        result = ""
        ### start the construction of the number
        result = thousand * "M" + result
        if hundre == 4 or hundre == 9:
            result = result + special_case[hundre * 100]
        else:
            if hundre < 5:
                result = result + num_dict[100] * hundre
            else:
                remind = hundre - 5
                result = result + num_dict[500] + num_dict[100] * remind
        if ten == 4 or ten == 9:
            result = result + special_case[ten * 10]
        else:
            if ten < 5:
                result = result + num_dict[10] * ten
            else:
                remind = ten - 5
                result = result + num_dict[50] + num_dict[10] * remind
        if digit == 4 or digit == 9:
            result = result + special_case[digit]
        else:
            if digit < 5:
                result = result + num_dict[1] * digit
            else:
                remind = digit - 5
                result = result + num_dict[5] + num_dict[1] * remind
        return result


solution = Solution()
print(solution.intToRoman(399))
print(solution.intToRoman(3))
print(solution.intToRoman(58))
print(solution.intToRoman(1994))
