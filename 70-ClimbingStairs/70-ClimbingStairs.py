# Last updated: 2/8/2026, 12:03:47 AM
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        0 - 0
        1 - 1
        2 - 2
        3 - 3
        4 - 5
        5 - 8
        6 - 13
        7 - 21
        """
        if (n<=3):
            return n
        a, b = 1, 1
        for x in range(n - 1):
            a, b = b, a + b
        return b

        