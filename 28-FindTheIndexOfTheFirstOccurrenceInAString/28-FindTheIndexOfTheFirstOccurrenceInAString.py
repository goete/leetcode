# Last updated: 2/8/2026, 12:03:51 AM
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            s = haystack[i:i + len(needle)]
            if (s == needle): return i
        return -1