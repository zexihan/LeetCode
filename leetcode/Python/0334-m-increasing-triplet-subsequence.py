"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
