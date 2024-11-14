class Solution:
    def longestNiceSubstring(self, s):
        if len(s) < 2:
            return ""
        
        for i in range(len(s)):
            c = s[i]
            if s.find(c.lower()) == -1 or s.find(c.upper()) == -1:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                return left if len(left) >= len(right) else right
        
        return s
