class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(0, n - 2):
            if i > 0  and nums[i] == nums[i-1]:
                continue
            if nums[i]>0:
                break
            left = i+1
            right = n-1
            ni = nums[i]
            while left < right:
                k = ni + nums[left] + nums[right]
                if k == 0:
                    ans.append([ni, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif k < 0:
                    left += 1
                else :
                    right -= 1            
        return ans