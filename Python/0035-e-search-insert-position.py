# Time:
# Space:
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0 , len(nums)-1
        while start <= end: 
            mid = (start+end)//2 
            if nums[mid] >= target: 
                end = mid - 1 
            elif nums[mid] < target: 
                start = mid+1 
        return start