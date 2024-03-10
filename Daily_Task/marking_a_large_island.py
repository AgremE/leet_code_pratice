# Problem 827
class Solution(object):
    def largestIsland(self, grid):
        """
        Algorithm:
        construct a graph and looking for connected sub-components
        For each sub componet, if the node has connected to at least one zero, it is boundary node
        we collect all this boundary nodes for sub component, for each of zero, construct
        a dictionary that inform which node will be connected if that node turn to 1
        from this point, we just aggregate the number of node with each sub components 
        that connected when the node turn into 1
        :type grid: List[List[int]]
        :rtype: int
        """
