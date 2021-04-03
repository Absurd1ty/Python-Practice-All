"""Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string."""

class Solution:
    def restoreString(self, s: str, indices: [int]):
        shuffled_string = ['']*len(s)
        for i in range (len(s)):
            shuffled_string[indices[i]] = s[i]
        return "".join(shuffled_string)

result = Solution().restoreString("aiohn", [3,1,4,2,0])
print(result)

"""Runtime: 40 ms, faster than 99.78% of Python3 online submissions for Shuffle String.
Memory Usage: 14.1 MB, less than 79.90% of Python3 online submissions for Shuffle String."""