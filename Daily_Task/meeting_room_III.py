from typing import List
import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings,key=lambda x: x[0])
        keep_count = [0 for _ in range(n)]
        next_meeting_removal = []
        heapq.heapify(next_meeting_removal)
        cur_room = 0
        re_init_room = []
        for meeting in meetings:
            s_t, e_t = meeting
            if next_meeting_removal:
                while next_meeting_removal:
                    n_m = heapq.heappop(next_meeting_removal)
                    e_t_last = (n_m[0]-n_m[1])//(10**9)
                    if s_t >= e_t_last:
                        re_init_room.append(n_m[1])
                    else:
                        break
                re_init_room = sorted(re_init_room)
                if len(next_meeting_removal)<n:
                    n_m = heapq.heappop(next_meeting_removal) # n_m is [end_time,room_n]
                    if (n_m[0]-n_m[1])<=s_t*(10**9):
                        heapq.heappush(next_meeting_removal,(e_t*10**9+n_m[1],n_m[1]))
                        keep_count[n_m[1]]+=1
                    else:
                        heapq.heappush(next_meeting_removal,n_m)
                        heapq.heappush(next_meeting_removal,(e_t*10**9+cur_room,cur_room))
                        keep_count[cur_room]+=1
                        cur_room +=1
                else:
                    # this is where delay happens
                    # find suitable index of room
                    n_m = heapq.heappop(next_meeting_removal) # n_m is [end_time,room_n]
                    e_t += max(0,(n_m[0]-n_m[1])//(10**9)-s_t)
                    heapq.heappush(next_meeting_removal,(e_t*10**9+n_m[1],n_m[1]))
                    keep_count[n_m[1]]+=1
            else:
                heapq.heappush(next_meeting_removal,(e_t*10**9+cur_room,cur_room))
                cur_room = 0
                keep_count[cur_room]+=1
                cur_room +=1
        _max = max(keep_count)
        for i in range(len(keep_count)):
            if keep_count[i] == _max:
                return i

solution = Solution()
print(solution.mostBooked(n = 4, meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]]  ))


# Code Leet
from heapq import *
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused_rooms, used_rooms = list(range(n)), []
        heapify(unused_rooms)
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(unused_rooms, room)
            if unused_rooms:
                room = heappop(unused_rooms)
                heappush(used_rooms, [end, room])
            else:
                room_availability_time, room = heappop(used_rooms)
                heappush(
                    used_rooms,
                    [room_availability_time + end - start, room]
                )
            meeting_count[room] += 1
        return meeting_count.index(max(meeting_count))

                                



