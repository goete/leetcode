// Last updated: 2/8/2026, 12:03:36 AM
class Solution {
    public String winningPlayer(int x, int y) {
        int maxTurns = (x > y/4) ? y/4 : x;
        return (maxTurns % 2 == 0) ? "Bob" : "Alice";
    }
}