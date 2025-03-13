class Solution {
    public void moveZeroes(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                int next = nextNonZero(nums, i);
                if (next < 0) break;
                nums[i] = nums[next];
                nums[next] = 0;
            }
        }
    }

    private int nextNonZero(int[] nums, int i) {
        while (i < nums.length) {
            if (nums[i] != 0) {
                return i;
            }
            i++;
        }
        return -1;
    }
}