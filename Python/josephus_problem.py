# normilization is done for CIRCULAR problems
#VERY IMPORTANT 

def helper(self, n,k):
    if n == 1:
        return 0
    return (helper(n-1,k) + k) % n

def josephus(self , n, k):
    winner = self.helper(n, k) + 1 #1-based index
    return winner


print(josephus(7, 3))  