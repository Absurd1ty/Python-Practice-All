"""Given a string s of zeros and ones, return the maximum score after 
splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring 
plus the number of ones in the right substring."""


class Solution:
    def maxScore(self, s: str):
        current_0s, current_1s, total_1s = 0, 0, 0
        for c in s:
            if c == '1':
                total_1s += 1
        
        maxScore = 0
        for c in s[:-1]:
            if c == '0':
                current_0s += 1
            else:
                current_1s += 1
            maxScore = max(maxScore, current_0s + total_1s - current_1s)
                
        return maxScore

result = Solution().maxScore("1010101")
print(result)