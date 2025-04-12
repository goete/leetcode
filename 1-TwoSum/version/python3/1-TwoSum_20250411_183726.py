# Last updated: 4/11/2025, 6:37:26 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in visited:
                return [visited[rem], i]
            visited[num] = i


        