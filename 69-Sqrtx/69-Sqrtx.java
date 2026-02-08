// Last updated: 2/8/2026, 12:03:48 AM
class Solution {
    public int mySqrt(int x) {
        if (x == 0){
            return 0;
        } else if (x == 1) {
            return 1;
        }
        long bottom = 1;

        while (true) {
            if (bottom * bottom <= x && (bottom+1)*(bottom+1) > x) {
                return (int) bottom;
            }
            bottom++;
            }
        
    }
}