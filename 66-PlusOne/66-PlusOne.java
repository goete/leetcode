// Last updated: 2/8/2026, 12:03:48 AM
class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length - 1;
        boolean cont = true;
        while (cont && n >= 0) {
            digits[n] += 1;
            if (digits[n] == 10) {
                digits[n] = 0;
                n--;
            } else {
                return digits;
            }
        }
        int[] ans = new int[digits.length + 1];
        ans[0] = 1;
        return ans;
    }
}