# Problem: Container With Most Water (LeetCode #11)
# Difficulty: Medium
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0
        
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            max_water = max(max_water, w * h)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_water