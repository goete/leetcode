class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int sum = 0;
        for (int i : hours) {
            if (i >= target) sum++;
        }
        return sum;
    }
}