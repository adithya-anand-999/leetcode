class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
            # path comphrehension as the parent of the node should be absolute, all nodes in a group only go up 1 level. 
            # If I called find on each node in a group I would reduce the height of the group to 1 as all the nodes that are not parent would point directlly to parent and not intermediate nodes. 
            # We dont update rank as rank is just an approximation of the height of the group, used only for the union method. 
        return self.parent[x]
    def union(self,x,y):
        r_x, r_y = self.find(x), self.find(y)

        if r_x != r_y:
            if self.rank[r_x] > self.rank[r_y]:
                self.parent[r_y] = r_x
            elif self.rank[r_x] < self.rank[r_y]:
                self.parent[r_x] = r_y
            else:
                self.parent[r_y] = r_x
                self.rank[r_x]+=1
            return True
        return False


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_acc = {}

        for i,a in enumerate(accounts):
            for e in a[1:]:
                if e in email_to_acc:
                    uf.union(i,email_to_acc[e]) #The sets are indicies of the accounts
                else:
                    email_to_acc[e] = i

        res = defaultdict(list)
        for e,i in email_to_acc.items():
            parent = uf.find(i)
            res[parent].append(e) #dont have the name of account at index as key now, as names can be shared between accounts
        print(res)
        res_list = []
        for i,emails in res.items():
            res_list.append([accounts[i][0]] + sorted(emails))
        return res_list