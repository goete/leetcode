# Last updated: 2/8/2026, 12:03:54 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in visited:
                return [visited[rem], i]
            visited[num] = i


        