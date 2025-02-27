class UnionFind:
    def __init__(self,n):
        self.pars = list(range(n))
        self.rank = [0]*n
    def find(self,x):
        if self.pars[x] != x:
            self.pars[x] = self.find(self.pars[x])
        return self.pars[x]
    def union(self,x,y):
        r_x,r_y = self.find(x),self.find(y)

        if r_x != r_y:
            if self.rank[r_x] < self.rank[r_y]:
                self.pars[r_x] = r_y
            elif self.rank[r_x] > self.rank[r_y]:
                self.pars[r_y] = r_x
            else:
                self.pars[r_x] = r_y
                self.rank[r_y]+=1
            return True
        return False 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        
        email_map = {}
        for i,a in enumerate(accounts):
            for e in a[1:]:
                if e in email_map:
                    uf.union(i,email_map[e])
                else:
                    email_map[e] = i
        
        acc_map = defaultdict(list)
        for e,i in email_map.items():
            par = uf.find(i)
            acc_map[par].append(e)
        
        res = []
        for i,emails in acc_map.items():
            res.append([accounts[i][0]] + sorted(emails))
        return res