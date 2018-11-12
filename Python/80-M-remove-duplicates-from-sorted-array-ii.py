class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        newTail = 0
        times = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]
                times = 1
            else:
                times += 1
                if times <= 2:
                    newTail += 1
                    nums[newTail] = nums[i]
        return newTail + 1

