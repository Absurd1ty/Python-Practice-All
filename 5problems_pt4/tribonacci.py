"""The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 """
class Solution:
    d={}
    def tribonacci(self, n: int):
        if(n==0):
            return 0
        elif(n==1 or n==2):
            return 1
        if n not in self.d.keys():
            self.d[n] = self.tribonacci(n-2) + self.tribonacci(n-1) + self.tribonacci(n-3)
        return self.d[n]
result = Solution().tribonacci(3)
print(result)