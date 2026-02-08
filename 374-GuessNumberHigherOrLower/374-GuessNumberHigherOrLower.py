# Last updated: 2/8/2026, 12:03:39 AM
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.guessNumRec(0, n)

    def guessNumRec(self, lower, upper):
        mid = lower + (upper - lower)/2
        ans = guess(mid)
        if (ans == 0):
            return mid
        if (ans == -1):
            return self.guessNumRec(lower, mid - 1)
        return self.guessNumRec(mid + 1, upper)