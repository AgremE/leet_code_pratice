from typing import List
class Solution:
    # 
    # This solution work but too slow
    # #
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meeting_dict = {}
        for meeting in meetings:
            if meeting[2] in meeting_dict:
                for i in range(len(meeting_dict[meeting[2]])):
                    conn = meeting_dict[meeting[2]][i]
                    found=False
                    if (meeting[0] in conn) or (meeting[1] in conn):
                        meeting_dict[meeting[2]][i].add(meeting[0])
                        meeting_dict[meeting[2]][i].add(meeting[1])
                        found = True
                if not found:
                    meeting_dict[meeting[2]].append(set([meeting[0],meeting[1]]))
            else:
                meeting_dict[meeting[2]] = [set([meeting[0],meeting[1]])]
        current_secret_holder = set([0,firstPerson])
        meeting_time = sorted(list(meeting_dict.keys()))
        for time in meeting_time:
            for conn in meeting_dict[time]:
                if current_secret_holder.intersection(conn):
                    current_secret_holder = current_secret_holder.union(conn)
        return list(current_secret_holder)

from typing import List
from math import inf 
from collections import defaultdict, deque
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # For every person, store the time and label of the person met.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))
        
        # Earliest time at which a person learned the secret 
        # as per current state of knowledge. If due to some new information, 
        # the earliest time of knowing the secret changes, we will update it
        # and again process all the people whom he/she meets after the time
        # at which he/she learned the secret.
        earliest = [inf] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        # Queue for BFS. It will store (person, time of knowing the secret)
        q = deque()
        q.append((0, 0))
        q.append((firstPerson, 0))

        # Do BFS
        while q:
            person, time = q.popleft()
            for t, next_person in graph[person]:
                if t >= time and earliest[next_person] > t:
                    earliest[next_person] = t
                    q.append((next_person, t))
        
        # Since we visited only those people who know the secret,
        # we need to return indices of all visited people.
        return [i for i in range(n) if earliest[i] != inf]

# Priority quque solution
from heapq import heapify, heappush, heappop
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # For every person, store the time and label of the person met.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        # Priority Queue for BFS. It stores (time secret learned, person)
        # It pops the person with the minimum time of knowing the secret.
        pq = []
        heappush(pq, (0, 0))
        heappush(pq, (0, firstPerson))

        # Visited array to mark if a person is visited or not.
        # We will mark a person as visited after it is dequeued
        # from the queue.
        visited = [False] * n

        # Do BFS, but pop minimum.
        while pq:
            time, person = heappop(pq)
            if visited[person]:
                continue
            visited[person] = True
            for t, next_person in graph[person]:
                if not visited[next_person] and t >= time:
                    heappush(pq, (t, next_person))

        # Since we visited only those people who know the secret
        # we need to return indices of all visited people.
        return [i for i in range(n) if visited[i]]
solution = Solution()
print(solution.findAllPeople(n=6,meetings=[[0,2,1],[1,3,1],[4,5,1]],firstPerson=1))