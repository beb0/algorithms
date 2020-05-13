class QuickUnion:
    def __init__(self, N):
        self.id = []
        for i in range(N):
            self.id.append(i)

    def root(self, num):
        while self.id[num] != num:
            num = self.id[num]
        return num
    
    def connnected(self, first, second):
        return self.root(first) == self.root(second)

    def union(self, p, q):
        self.p1 = self.root(p)
        self.q2 = self.root(q)

        self.id[self.q2] = self.p1