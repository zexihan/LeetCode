"""
Moore Voting
这是一种先假设候选者，然后再进行验证的算法。我们现将数组中的第一个数假设为过半数，
然后进行统计其出现的次数，如果遇到同样的数，则计数器自增1，否则计数器自减1，如果计
数器减到了0，则更换下一个数字为候选者。这是一个很巧妙的设定，也是本算法的精髓所在，
为啥遇到不同的要计数器减1呢，为啥减到0了又要更换候选者呢？首先是有那个强大的前提存
在，一定会有一个出现超过半数的数字存在，那么如果计数器减到0了话，说明目前不是候选者
数字的个数已经跟候选者的出现个数相同了，那么这个候选者已经很weak，不一定能出现超过
半数，我们选择更换当前的候选者。那有可能你会有疑问，那万一后面又大量的出现了之前的候
选者怎么办，不需要担心，如果之前的候选者在后面大量出现的话，其又会重新变为候选者，直
到最终验证成为正确的过半数.
Time: O(n)
Space: O(1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

"""
HashMap
Time: O(n)
Space: O(n)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)