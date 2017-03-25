"""
133. Clone Graph
DescriptionSubmissionsSolutions
Total Accepted: 102194
Total Submissions: 407540
Difficulty: Medium
Contributors: Admin
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
Subscribe to see which companies asked this question.

Hide Tags Depth-first Search Breadth-first Search Graph
Hide Similar Problems (M) Copy List with Random Pointer

"""

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def cloneGraph(self, node):

        if not node:
            return node
        # copy node
        root = UndirectedGraphNode(node.label)
        # push node into a stack
        stack = [node]
        # store node.label and node in visit
        visit = {}
        visit[node.label] = root
        while stack:
            top = stack.pop()
            for n in top.neighbors:
                # new label
                if n.label not in visit:
                    # push into stack
                    stack.append(n)
                    # store it in visit as a new copied node
                    visit[n.label] = UndirectedGraphNode(n.label)
                # set the label as the top.label's neighbors.
                visit[top.label].neighbors.append(visit[n.label])

        return root
