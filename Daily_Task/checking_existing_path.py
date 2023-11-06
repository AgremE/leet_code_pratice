from typing import List


def construct_graph(edge: list):
    """
    From edge list to construct graph, with edge of the following format
    [v1,v2,weight]. There will be multiple edge from one v1 to v2. Selected the smallest one
    """
    graph = {}
    for v1, v2, weight in edge:
        if v1 not in graph:
            graph[v1] = {}
        if v2 not in graph:
            graph[v2] = {}
        if v2 not in graph[v1]:
            graph[v1][v2] = weight
        else:
            graph[v1][v2] = min(graph[v1][v2], weight)
    return graph


def dijkstra(graph: dict, start: int, end: int):
    """
    From graph input to find the shortest path from start to end
    Graph: dict with graph[v1][v2] =weighted
    start: int start vertext
    end: int start vertext
    """
    ### Initialize the distance and path
    distance = {}
    path = {}
    for v in graph:
        distance[v] = float("inf")
        path[v] = []
    distance[start] = 0
    path[start] = [start]
    ### Initialize the queue
    queue = []
    for v in graph:
        queue.append(v)
    ### Start the iteration
    while queue:
        ### Find the vertex with the smallest distance
        min_distance = float("inf")
        min_vertex = None
        for v in queue:
            if distance[v] < min_distance:
                min_distance = distance[v]
                min_vertex = v
        ### Remove the vertex from queue
        queue.remove(min_vertex)
        ### Update the distance and path
        for v in graph[min_vertex]:
            if distance[v] > distance[min_vertex] + graph[min_vertex][v]:
                distance[v] = distance[min_vertex] + graph[min_vertex][v]
                path[v] = path[min_vertex] + [v]
    return distance[end], path[end]


def generate_dict_pair(query: list):
    """
    from query with following format:
    [v1,v2,limited_weight], generated the list with following format:
    unique pair [v1,v2] regardless of the order
    """
    pair_dict = []
    already_added = {}
    for v1, v2, weight in query:
        if (v1, v2) in already_added or (v2, v1) in already_added:
            continue
        pair_dict.append((v1, v2))
        already_added[(v1, v2)] = True
    return pair_dict


def distanceLimitedPathsExist(
    n: int, edgeList: List[List[int]], queries: List[List[int]]
) -> List[bool]:
    graph = construct_graph(edgeList)
    print(graph)
    pair_dict = generate_dict_pair(queries)
    min_distance_needed = {}
    for v1, v2 in pair_dict:
        min_distance_needed[(v1, v2)] = dijkstra(graph, v1, v2)[0]
        min_distance_needed[(v2, v1)] = min_distance_needed[(v1, v2)]
    result = []
    for qry in queries:
        v1, v2, limited_weight = qry
        if min_distance_needed[(v1, v2)] >= limited_weight:
            result.append(False)
        else:
            result.append(True)
    return result


print(
    distanceLimitedPathsExist(
        n=5,
        edgeList=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
        queries=[[0, 4, 14], [1, 4, 13]],
    )
)
