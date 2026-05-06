class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        current_amount = 0
        n = len(heights)
        for i in range(0, n-1):
            r = n-1
            while i < r :
                h = min(heights[i], heights[r])
                current_amount = h*(r-i)
                max_amount = max(max_amount, current_amount)
                r -= 1
        return max_amount