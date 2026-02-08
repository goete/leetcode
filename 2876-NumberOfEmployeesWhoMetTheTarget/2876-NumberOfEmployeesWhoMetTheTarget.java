// Last updated: 2/8/2026, 12:03:33 AM
class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int sum = 0;
        for (int i : hours) {
            if (i >= target) sum++;
        }
        return sum;
    }
}