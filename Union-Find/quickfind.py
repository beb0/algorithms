class QuickFind:
    def __init__(self,N):
        self.lis = []
        for i in range(N):
            self.lis.append(i)

    def connected(self, p, q):
        return self.lis[p] == self.lis[q]

    def union(self, p, q):
       lisp = self.lis[p]
       lisq = self.lis[q]
       for i in range(len(self.lis)):
           if self.lis[i] == lisp:
               self.lis[i] = lisq

    def check(self):
        print(self.lis)