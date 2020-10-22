"""Given a List of words, return the words that can be typed
 using letters of alphabet on only one row's of American keyboard like the image below.

 """

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = set('qwertyuiopQWERTYUIOP')
        middle = set('asdfghjklASDFGHJKL')
        bottom = set('zxcvbnmZXCVBNM')
        typable = []
        for word in words:
            
            w = set(word)
            
            if w.issubset(top) or w.issubset(middle) or w.issubset(bottom):

                typable.append(word)
                
        return typable