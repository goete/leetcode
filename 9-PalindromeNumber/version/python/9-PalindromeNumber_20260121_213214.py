# Last updated: 1/21/2026, 9:32:14 PM
1class Solution(object):
2    def isPalindrome(self, x):
3        """
4        :type x: int
5        :rtype: bool
6        """
7        return str(x) == str(x)[::-1]