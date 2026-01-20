# Last updated: 1/19/2026, 10:06:09 PM
1class Solution(object):
2    def lengthOfLastWord(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        return len(s.strip().split()[-1])