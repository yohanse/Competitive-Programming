class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        tree =  [[] for i in range(n)]

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def postorder(parent, node):
            if tree[node] == [parent]:
                return 1, 1

            total_good_nodes = 0
            total_nodes = 0
            subtree_num_nodes = -1
            for child in tree[node]:
                if child != parent:
                    nodes_num, good_nodes_num = postorder(node, child)
                    if subtree_num_nodes == -1 or subtree_num_nodes == nodes_num:
                        subtree_num_nodes = nodes_num
                    else:
                        subtree_num_nodes = -2

                    total_good_nodes += good_nodes_num
                    total_nodes += nodes_num
            
            if subtree_num_nodes != -2:
                total_good_nodes += 1
            return total_nodes + 1, total_good_nodes
        
        return postorder(-1, 0)[1]
