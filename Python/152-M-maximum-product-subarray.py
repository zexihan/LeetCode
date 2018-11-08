class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # store the result that is the max we have found so far
        r = nums[0]

        # imax/imin stores the max/min product of
        # subarray that ends with the current number nums[i]
        imax, imin = r, r
        for i in range(1, len(nums)):
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            if nums[i] < 0:
                tmp = imax
                imax = imin
                imin = tmp

            # max/min product for the current number is either the current number itself
            # or the max/min by the previous number times the current one
            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])

            # the newly computed max value is a candidate for our global result
            r = max(r, imax)
        return r