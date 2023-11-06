from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        track_cluster = {}
        cluster_info = {"num_id_cluster": 0}
        tracker_cells = {}

        cells = [[x[1], x[0]] for x in cells]
        temp = row
        row = col
        col = temp

        def get_surr_coors(x, y, max_x, max_y):
            result = [
                [x + 1, y],
                [x + 1, y + 1],
                [x + 1, y - 1],
                [x - 1, y + 1],
                [x - 1, y],
                [x - 1, y - 1],
                [x, y + 1],
                [x, y - 1],
            ]
            neighboor = [
                x
                for x in result
                if (x[0] > 0) and (x[1] > 0) and (x[0] <= max_x) and (x[1] <= max_y)
            ]
            return neighboor

        def combine_cluster(cluster_info, tracker, tracker_cells, combine_list, cell):
            cluster_id = 0
            if not combine_list:
                cluster_id = cluster_info["num_id_cluster"] + 1
                cluster_info["num_id_cluster"] = cluster_id
                cluster_info[cluster_id] = {
                    "max_x": cell[0],
                    "min_x": cell[0],
                    "num_elem": 1,
                    "width": 1,
                }
                tracker[cell] = cluster_id
                tracker_cells[cluster_id] = [cell]
            elif len(combine_list) == 1:
                cluster_id = combine_list[0]
                cluster_information_id = cluster_info[cluster_id]
                cluster_info[cluster_id] = {
                    "max_x": max(cluster_information_id["max_x"], cell[0]),
                    "min_x": min(cluster_information_id["min_x"], cell[0]),
                    "num_elem": cluster_information_id["num_elem"] + 1,
                    "width": max(cluster_information_id["max_x"], cell[0])
                    - min(cluster_information_id["min_x"], cell[0])
                    + 1,
                }
                tracker[cell] = cluster_id
                tracker_cells[cluster_id].append(cell)
            else:
                max_cluster = 0
                max_cluster_id = 0
                for cluster_id in combine_list:
                    if cluster_info[cluster_id]["num_elem"] > max_cluster:
                        max_cluster = cluster_info[cluster_id]["num_elem"]
                        max_cluster_id = cluster_id
                for cluster_id in combine_list:
                    if cluster_id != max_cluster_id:
                        max_x = cluster_info[cluster_id]["max_x"]
                        min_x = cluster_info[cluster_id]["min_x"]
                        num_elem = cluster_info[cluster_id]["num_elem"]

                        max_x_centroid_cluster = cluster_info[max_cluster_id]["max_x"]
                        min_x_centroid_cluster = cluster_info[max_cluster_id]["min_x"]
                        num_elem_centroid_cluster = cluster_info[max_cluster_id][
                            "num_elem"
                        ]

                        new_max_x = max([max_x, max_x_centroid_cluster, cell[0]])
                        new_min_x = min([min_x, min_x_centroid_cluster, cell[0]])
                        width_centroid_cluster = new_max_x - new_min_x + 1
                        new_num_elem = num_elem + num_elem_centroid_cluster
                        cluster_info[max_cluster_id] = {
                            "max_x": new_max_x,
                            "min_x": new_min_x,
                            "num_elem": new_num_elem,
                            "width": width_centroid_cluster,
                        }
                for cluster_id in combine_list:
                    if cluster_id != max_cluster_id:
                        cells_list = tracker_cells[cluster_id]
                        for _cell in cells_list:
                            tracker[_cell] = max_cluster_id
                        tracker_cells[max_cluster_id] = list(
                            set(
                                tracker_cells[cluster_id]
                                + tracker_cells[max_cluster_id]
                            )
                        )
                        del cluster_info[cluster_id]
                        del tracker_cells[cluster_id]

                tracker[cell] = max_cluster_id
                tracker_cells[max_cluster_id].append(cell)
                cluster_id = max_cluster_id
            return (cluster_info, tracker, tracker_cells, cluster_id)

        track_day = 0
        for cell in cells:
            x, y = cell
            nb_ls = get_surr_coors(x, y, row, col)
            cluster_restruc_list = []
            track_day = track_day + 1
            ### Checkoing for cluster if exist
            for nb in nb_ls:
                nb_x, nb_y = nb
                if (nb_x, nb_y) in track_cluster:
                    cluster_restruc_list.append(track_cluster[(nb_x, nb_y)])
            cluster_restruc_list = list(set(cluster_restruc_list))
            (
                cluster_info,
                track_cluster,
                tracker_cells,
                cluster_number,
            ) = combine_cluster(
                cluster_info,
                track_cluster,
                tracker_cells,
                cluster_restruc_list,
                (cell[0], cell[1]),
            )
            if cluster_info[cluster_number]["width"] >= row:
                return track_day - 1
        return track_day - 1


solution = Solution()
print(
    solution.latestDayToCross(
        row=25,
        col=4,
        cells=[
            [17, 2],
            [1, 4],
            [12, 2],
            [23, 3],
            [4, 2],
            [1, 2],
            [21, 2],
            [13, 3],
            [7, 4],
            [3, 1],
            [24, 3],
            [16, 1],
            [19, 1],
            [7, 1],
            [18, 1],
            [6, 2],
            [21, 3],
            [22, 2],
            [15, 2],
            [1, 3],
            [5, 2],
            [4, 4],
            [20, 4],
            [24, 4],
            [20, 1],
            [14, 3],
            [10, 3],
            [23, 4],
            [6, 4],
            [17, 3],
            [20, 2],
            [1, 1],
            [17, 4],
            [18, 2],
            [10, 1],
            [25, 1],
            [11, 4],
            [12, 4],
            [7, 2],
            [3, 2],
            [2, 1],
            [18, 3],
            [14, 2],
            [24, 2],
            [25, 2],
            [7, 3],
            [19, 4],
            [9, 3],
            [16, 3],
            [11, 3],
            [18, 4],
            [5, 1],
            [11, 2],
            [13, 2],
            [14, 1],
            [9, 2],
            [12, 3],
            [21, 1],
            [16, 2],
            [19, 2],
            [24, 1],
            [6, 3],
            [22, 4],
            [15, 4],
            [11, 1],
            [6, 1],
            [13, 4],
            [3, 3],
            [5, 4],
            [22, 1],
            [12, 1],
            [22, 3],
            [9, 1],
            [16, 4],
            [20, 3],
            [8, 3],
            [9, 4],
            [19, 3],
            [2, 2],
            [2, 3],
            [10, 4],
            [3, 4],
            [4, 3],
            [8, 2],
            [2, 4],
            [17, 1],
            [13, 1],
            [4, 1],
            [25, 4],
            [25, 3],
            [23, 2],
            [15, 1],
            [21, 4],
            [14, 4],
            [8, 1],
            [23, 1],
            [8, 4],
            [15, 3],
            [5, 3],
            [10, 2],
        ],
    )
)
