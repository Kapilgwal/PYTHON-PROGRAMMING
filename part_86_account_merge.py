class DisjointSet:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n 
        
    def findUParent(self, node: int):
        if self.parent[node] == node:
            return node
        # Path compression
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)
        
        if ulp_u == ulp_v:
            return 
        
        # Union by rank
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        
        else:
            self.parent[ulp_u] = ulp_v
            self.rank[ulp_v] += 1
            
def mergeAccounts(accounts: list[list[str]], n: int) -> list[list[str]]:
    ds = DisjointSet(n)
    mapMailNode = {}

    # Map mails to nodes and perform unions
    for i in range(n):
        for j in range(1, len(accounts[i])):
            mail = accounts[i][j]
            if mail not in mapMailNode:
                mapMailNode[mail] = i
            else:
                ds.unionByRank(i, mapMailNode[mail])

    # Prepare merged mail lists
    mergedMail = [[] for _ in range(n)]
    
    for mail, accIndex in mapMailNode.items():
        rootIndex = ds.findUParent(accIndex)
        mergedMail[rootIndex].append(mail)

    # Prepare final answer
    ans = []
    
    for i in range(n):
        if len(mergedMail[i]) == 0:
            continue
        # Sort mails and prepend the name of the account holder
        mergedMail[i].sort()
        temp = [accounts[i][0]] + mergedMail[i]
        ans.append(temp)
    
    return ans
    
def main():
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    
    N = len(accounts)
    result = mergeAccounts(accounts, N)
    
    for account in result:
        print(account)

if __name__ == "__main__":
    main()
