# Last updated: 2/8/2026, 12:03:43 AM
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = {}
        for obj in nums:
            if not obj in n:
                n[obj] = 1
            else:
                n[obj] += 1
        return max(n, key=n.get)