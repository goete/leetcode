# Last updated: 2/8/2026, 12:03:38 AM
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # culmativeA = 0
        # currLateStreak = 0
        # for c in s:
        #     if c == 'A':
        #         culmativeA += 1
        #     if c ==  'L':
        #         currLateStreak += 1
        #     else:
        #         currLateStreak = 0
        #     if culmativeA >= 2 or currLateStreak >= 3:
        #         return False
        # return True
        if 'LLL' in s:
            return False
        if s.count('A') >= 2:
            return False
        return True
        