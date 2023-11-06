# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
import heapq


class SeatManager:
    def __init__(self, n: int):
        self.reserve_list = [0 for _ in range(n + 1)]
        self.unreserve_list = []
        self.next_reserve = 1

    def reserve(self) -> int:
        if self.unreserve_list:
            lowest_seat = heapq.heappop(self.unreserve_list)
            if lowest_seat < self.next_reserve:
                self.reserve_list[lowest_seat] = 1
                return lowest_seat
            else:
                heapq.heappush(self.unreserve_list, lowest_seat)
        self.reserve_list[self.next_reserve] = 1
        return_seat = self.next_reserve
        self.next_reserve += 1
        return return_seat

    def unreserve(self, seatNumber: int) -> None:
        if self.reserve_list[seatNumber] != 0:
            self.reserve_list[seatNumber] = 0
            heapq.heappush(self.unreserve_list, seatNumber)


solution = SeatManager(5)
print(solution.reserve())
print(solution.reserve())
solution.unreserve(2)
print(solution.unreserve_list)
