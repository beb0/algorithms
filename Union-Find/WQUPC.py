class WQUPC:
    def __init__(self, N):
        self.id = []
        self.sz = []

        for i in range(N):
            self.sz.append(1)
            self.id.append(i)

    def root(self, num):
        while self.id[num] != num:
            self.id[num] = self.id[self.id[num]]
            num = self.id[num]
        return num
    
    def connnected(self, first, second):
        return self.root(first) == self.root(second)

    def union(self, p, q):
        self.p1 = self.root(p)
        self.q2 = self.root(q)

        if self.sz[p] > self.sz[q]:
            self.id[self.q2] = self.p1
            self.sz[p] += self.sz[q]
        else:
            self.id[self.p1] = self.q2
            self.sz[q] += self.sz[p]