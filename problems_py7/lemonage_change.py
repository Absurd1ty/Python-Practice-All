"""At a lemonade stand, each lemonade costs $5. 
Customers are standing in a queue to buy from you, and order one at a time 
(in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  
You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
Note that you don't have any change in hand at first.
Return true if and only if you can provide every customer with correct change.

"""
class Solution:
    def lemonadeChange(self, bills: [int]):
        five = 0
        ten = 0
        for i in bills:
            if i == 5: 
                five += 1
            elif i == 10: 
                five, ten = five - 1, ten + 1
            elif ten > 0: 
                five, ten = five - 1, ten - 1
            else: 
                five -= 3
            if five < 0: 
                return False
        return True