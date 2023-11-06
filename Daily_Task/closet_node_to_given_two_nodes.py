from typing import List
import json


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_distance_reachable(edges, node):
            already_visit = {}
            next_vertext = edges[node]
            already_visit[node] = 1
            already_visit[-1] = 1
            distinct = {}
            distinct[node] = 0
            if edges[node] == -1:
                return distinct
            distinct[edges[node]] = 1
            while next_vertext != -1:
                n_v = next_vertext
                if n_v in already_visit or n_v == -1:
                    break
                else:
                    if edges[n_v] == -1 or edges[n_v] in already_visit:
                        break
                    next_vertext = edges[n_v]
                    distinct[edges[n_v]] = distinct[n_v] + 1
                    already_visit[n_v] = 1
            return distinct

        distinct_node_1 = get_distance_reachable(edges, node1)
        distinct_node_2 = get_distance_reachable(edges, node2)
        min_value = float("inf")
        result_list = []
        for node, value in distinct_node_1.items():
            if not (node in distinct_node_2):
                continue
            value_2 = distinct_node_2[node]
            max_value = max([value_2, value])
            if max_value < min_value:
                min_value = max_value
                result_list = [node]
            elif max_value == min_value:
                result_list.append(node)
        if not result_list:
            return -1
        return min(result_list)


solution = Solution()
data = {}
with open("../Data/test.json") as json_file:
    data = json.load(json_file)
print(solution.closestMeetingNode(data["edges"], data["node_1"], data["node_2"]))
