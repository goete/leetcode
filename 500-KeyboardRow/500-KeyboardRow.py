# Last updated: 2/8/2026, 12:03:39 AM
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        top = "qwertyuiop"
        middle = "asdfghjkl"
        bottom = "zxcvbnm"
        ans = []
        for word in words:
            wordLower = word.lower()
            if set(wordLower).issubset(set(top)) or set(wordLower).issubset(set(middle)) or set(wordLower).issubset(set(bottom)):
                ans += [word]
        return ans