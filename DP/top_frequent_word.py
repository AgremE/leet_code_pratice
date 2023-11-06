from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freque_count = [0 for _ in range(len(words) + 1)]
        dict_wordcount = {}
        for word in words:
            if word in dict_wordcount:
                dict_wordcount[word] = dict_wordcount[word] + 1
            else:
                dict_wordcount[word] = 1
        for _k, v in dict_wordcount.items():
            if freque_count[v] == 0:
                freque_count[v] = []
                freque_count[v].append(_k)
            else:
                freque_count[v].append(_k)
        for i in range(len(words) + 1):
            if freque_count[i] == 0:
                continue
            else:
                freque_count[i].sort()

        result = []
        remind = k
        for _i in reversed(range(1, len(words) + 1)):
            if freque_count[_i] == 0:
                continue
            if remind - len(freque_count[_i]) >= 0:
                remind = remind - len(freque_count[_i])
                result = result + freque_count[_i]
            else:
                result = result + freque_count[_i][:remind]
                remind = 0
                break
        return result


solution = Solution()
# print(solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 1))
print(
    solution.topKFrequent(
        [
            "plpaboutit",
            "jnoqzdute",
            "sfvkdqf",
            "mjc",
            "nkpllqzjzp",
            "foqqenbey",
            "ssnanizsav",
            "nkpllqzjzp",
            "sfvkdqf",
            "isnjmy",
            "pnqsz",
            "hhqpvvt",
            "fvvdtpnzx",
            "jkqonvenhx",
            "cyxwlef",
            "hhqpvvt",
            "fvvdtpnzx",
            "plpaboutit",
            "sfvkdqf",
            "mjc",
            "fvvdtpnzx",
            "bwumsj",
            "foqqenbey",
            "isnjmy",
            "nkpllqzjzp",
            "hhqpvvt",
            "foqqenbey",
            "fvvdtpnzx",
            "bwumsj",
            "hhqpvvt",
            "fvvdtpnzx",
            "jkqonvenhx",
            "jnoqzdute",
            "foqqenbey",
            "jnoqzdute",
            "foqqenbey",
            "hhqpvvt",
            "ssnanizsav",
            "mjc",
            "foqqenbey",
            "bwumsj",
            "ssnanizsav",
            "fvvdtpnzx",
            "nkpllqzjzp",
            "jkqonvenhx",
            "hhqpvvt",
            "mjc",
            "isnjmy",
            "bwumsj",
            "pnqsz",
            "hhqpvvt",
            "nkpllqzjzp",
            "jnoqzdute",
            "pnqsz",
            "nkpllqzjzp",
            "jnoqzdute",
            "foqqenbey",
            "nkpllqzjzp",
            "hhqpvvt",
            "fvvdtpnzx",
            "plpaboutit",
            "jnoqzdute",
            "sfvkdqf",
            "fvvdtpnzx",
            "jkqonvenhx",
            "jnoqzdute",
            "nkpllqzjzp",
            "jnoqzdute",
            "fvvdtpnzx",
            "jkqonvenhx",
            "hhqpvvt",
            "isnjmy",
            "jkqonvenhx",
            "ssnanizsav",
            "jnoqzdute",
            "jkqonvenhx",
            "fvvdtpnzx",
            "hhqpvvt",
            "bwumsj",
            "nkpllqzjzp",
            "bwumsj",
            "jkqonvenhx",
            "jnoqzdute",
            "pnqsz",
            "foqqenbey",
            "sfvkdqf",
            "sfvkdqf",
        ],
        1,
    )
)
