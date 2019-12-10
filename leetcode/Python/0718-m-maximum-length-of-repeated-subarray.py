"""
DP
dp[i][j]: the longest common prefix of A[i:] and B[j:]
If A[i] == B[j], dp[i][j] = dp[i + 1][j + 1] + 1
answer: max(dp[i][j])
Time: O(mn)
Space: O(mn)
"""
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
        return max(max(row) for row in dp)