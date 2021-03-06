class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        width = max(0, min(C, G) - max(A, E))
        height = max(0, min(D, H) - max(B, F))
        return (C - A) * (D - B) + (G - E) * (H - F) - height * width