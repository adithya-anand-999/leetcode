class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return[0]

        # adjacency list, storing edges in a hashmap. Key is the node, values the connections it has. 
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # leaves are keys in graph that have a value of length 1, meaning 1 connection.
        leaves = deque([i for i in range(n) if len(graph[i]) == 1])\\

        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf =  leaves.popleft()
                # why loop over all neighbors of the leaf node, there can only be 1 neightbor else it would not be a leaf node or included in leaves.
                n = graph[leaf][0]
                # del graph[leaf]
                graph[n].remove(leaf)
                if len(graph[n]) == 1: leaves.append(n)



                #remove the leaf from the graph
                # for n in graph[leaf]:
                #     graph[n].remove(leaf)
                #     # if the parent of the leaf node (n) now becomes a leaf node add it to the leaf node queue
                #     if len(graph[n]) == 1:
                #         leaves.append(n)
        return list(leaves)