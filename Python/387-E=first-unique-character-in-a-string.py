# Time: O(n)
# Space: O(1)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - ord("a")] += 1
        for i in range(len(s)):
            if freq[ord(s[i]) - ord("a")] == 1:
                return i;
        return -1