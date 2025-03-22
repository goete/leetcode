// Last updated: 3/21/2025, 11:11:21 PM
class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = 1;
        Arrays.sort(nums);
        for (int i : nums) {
            if (i > 0 && i>=n) {
                if (n != i) return n;
                n++;
            }
        }
        return n;
    }
}