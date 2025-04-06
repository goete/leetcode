// Last updated: 4/6/2025, 1:14:25 AM
class Solution {
        public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) return 0;
        ArrayList<String> curr = options(beginWord, wordList);
        ArrayList<String> future = new ArrayList<String>();
        int num = 1;
        while (!curr.contains(endWord)) {
            while (!curr.isEmpty()) {
                future.addAll(options(curr.remove(0), wordList));
            }
            wordList.removeIf(future::contains);
            curr = future;
            future = new ArrayList<>();
            num++;
            if (curr.isEmpty()) return 0;
        }
        return num+1;
    }
    
    private ArrayList<String> options(String s, List<String> wordList) {
        ArrayList<String> ans = new ArrayList<>();
        for (String word : wordList) {
            if (oneOff(s, word)) ans.add(word);
        }
        return ans;
    }

    private boolean oneOff(String s, String word) {
        int num = 1;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != word.charAt(i)) num--;
            if (num < 0) return false;
        }
        return num == 0;
    }
}