"""Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students 
that must move in order for all students to be standing in non-decreasing order of height.

Notice that when a group of students is selected 
they can reorder in any possible way between themselves 
and the non selected students remain on their seats."""

 

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        heights_sorted = sorted(heights)
        moves = 0
        
        for i in range (len(heights)):
            if heights_sorted[i] != heights[i]:
                moves += 1 
        return moves