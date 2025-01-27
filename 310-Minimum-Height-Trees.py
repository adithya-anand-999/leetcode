class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return[0]
        tree = defaultdict(list)
        for a,b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        leaves = deque([i for i in range(n) if len(tree[i]) == 1])

        remains = n
        while remains > 2:
            num_leaves = len(leaves)
            remains-=num_leaves
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                n = tree[leaf][0]
                tree[n].remove(leaf)
                if len(tree[n]) == 1: leaves.append(n)
        return list(leaves)