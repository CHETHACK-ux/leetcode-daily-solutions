# Time: O(n) | Space: O(1) - Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]
        for n in nums:
            curr_sum = max(n, curr_sum + n)
            max_sum = max(max_sum, curr_sum)
        return max_sum