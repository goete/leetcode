class Solution {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<String>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '{' || s.charAt(i) == '(' || s.charAt(i) == '[') {
                stack.push(s.substring(i, i + 1));
            } else if (stack.isEmpty() || 
                        s.charAt(i) == '}' && !Objects.equals(stack.peek(), "{") ||
                        s.charAt(i) == ']' && !Objects.equals(stack.peek(), "[") ||
                        s.charAt(i) == ')' && !Objects.equals(stack.peek(), "(")) {
                    return false;
            } else {
                stack.pop();
            }
        }
        return stack.empty();
    }
}