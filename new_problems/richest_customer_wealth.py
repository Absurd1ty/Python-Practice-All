"""You are given an m x n integer grid accounts where accounts[i][j] is the amount 
of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth."""

class Solution:
     def maximumWealth(self, accounts: [[int]]):

         wealth = 0
         max_wealth = 0 
         for i in range (len(accounts)):
             wealth = sum(accounts[i])
             if wealth > max_wealth:
                 max_wealth = wealth
             else:
                 continue
        
         return max_wealth


"""Runtime: 52 ms, faster than 74.37% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 14.2 MB, less than 83.74% of Python3 online submissions for Richest Customer Wealth."""