"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali_range(i, j):
            return all(s[k] == s[j - k + i] for k in range(i, j))
        
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                j = len(s) - 1 - i
                return is_pali_range(i + 1, j) or is_pali_range(i, j - 1)
        return True