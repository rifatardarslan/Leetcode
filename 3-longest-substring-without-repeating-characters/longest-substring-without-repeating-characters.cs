public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int maxLen = 0;

        for (int i = 0; i < s.Length; i++) {
            int len = 0;
            for (int j = i; j < s.Length; j++) {
                bool duplicate = false;
                for (int k = i; k < j; k++) {
                    if (s[k] == s[j]) {
                        duplicate = true;
                        break;
                    }
                }
                if (duplicate) break;

                len++;
                if (len > maxLen)
                    maxLen = len;
            }
        }
        return maxLen;
    }
}
