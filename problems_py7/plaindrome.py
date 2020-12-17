"""Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here."""
class Solution:
    def longestPalindrome_set(self, s):
        letters = set()
        for letter in s:
            if letter not in letters:
                letters.add(letter)
            else:
                letters.remove(letter)
        if len(letters) != 0:
            return len(s) - len(letters) + 1
        else:
            return len(s)
        