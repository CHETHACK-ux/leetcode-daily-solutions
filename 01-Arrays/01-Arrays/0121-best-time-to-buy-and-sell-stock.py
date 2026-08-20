# Time: O(n) | Space: O(1)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_p = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_p:
                max_p = p - min_price
        return max_p