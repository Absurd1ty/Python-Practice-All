"""Suppose you have a long flowerbed 
in which some of the plots are planted and some are not. However, 
flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 
0 means empty and 1 means not empty), and a number n, return if n new 
flowers can be planted in it without violating the no-adjacent-flowers rule."""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    
        if n == 0: return True
        
        if len(flowerbed) == 0: 
            return False
        
        if len(flowerbed) == 1: 
            return flowerbed[0] == 0
            
     
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        
      
        i=0
        
        while i < len(flowerbed)-2 and n > 0:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                flowerbed[i+1] = 1
                n-=1
            i+=1
            
        return n == 0