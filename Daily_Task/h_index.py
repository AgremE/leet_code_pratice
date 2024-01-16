class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        h = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h += 1
        return h
