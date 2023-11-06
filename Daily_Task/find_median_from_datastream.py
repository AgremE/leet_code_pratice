from heapq import *


class MedianFinder:
    def __init__(self):
        self.arr = []
        self.total_len = 0

    def find_inx(self, arr, num) -> int:
        f_ind = 0
        end_ind = len(arr)
        if not arr:
            return 0
        mid_ind = 0
        while end_ind > f_ind:
            mid_ind = (f_ind + end_ind) // 2
            if end_ind - f_ind == 1:
                break
            if num >= arr[mid_ind]:
                f_ind = mid_ind
            elif num < arr[mid_ind]:
                end_ind = mid_ind
        if arr[mid_ind] < num:
            mid_ind = mid_ind + 1
        return mid_ind

    def addNum(self, num: int) -> None:
        insert_index = self.find_inx(self.arr, num)
        if insert_index >= self.total_len:
            self.arr.append(num)
        else:
            self.arr = self.arr[:insert_index] + [num] + self.arr[insert_index:]
        self.total_len = self.total_len + 1

    def findMedian(self) -> float:
        odd_case = True
        if self.total_len == 0:
            return None
        if self.total_len % 2 == 0:
            odd_case = False
        if not odd_case:
            mid_ind = self.total_len // 2
            return sum(self.arr[mid_ind - 1 : mid_ind + 1]) / 2
        else:
            mid_ind = self.total_len // 2
            return self.arr[mid_ind]


class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))

    def findMedian(self) -> float:

        if (len(self.maxHeap) + len(self.minHeap)) % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        return -self.maxHeap[0]


medianFinder = MedianFinder()
# print(medianFinder.find_inx([1, 2], 3))

# print(medianFinder.findMedian())
medianFinder.addNum(-1)  # arr = [1]
# print(medianFinder.findMedian())
medianFinder.addNum(-2)  # arr = [1, 2]
# print(medianFinder.findMedian())  # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(-3)  # arr[1, 2, 3]
print(medianFinder.findMedian())  # return 2.0
medianFinder.addNum(-4)
print(medianFinder.findMedian())
medianFinder.addNum(-5)
print(medianFinder.findMedian())
