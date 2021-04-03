"""Given a string s and a character c that occurs in s, 
  return an array of integers answer where answer.length == 
  s.length and answer[i] is the distance from index i to the 
  closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function."""
  
def shortestToChar(self, s, c):
    result = []
    position = [] 
    for i in range(len(s)):
        if s[i] == c:
            position.append(i)                
    for i in range(len(s)):
        distance = len(s) 
        for p in position:                
            distance = min(distance, abs(i-p)) 
        result.append(distance)
    return result