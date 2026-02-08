# Last updated: 2/8/2026, 12:03:42 AM
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(curr, visited):
            if curr in visited: 
                return False
            if curr == 1:
                return True
            visited += [curr]
            nextNum = sum(int(c) ** 2 for c in str(curr))
            return helper(nextNum, visited)

        return helper(n, [])