class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        freq = [[] for i in range(len(nums)+1)]
        for num, c in count.items():
            freq[c].append(num)
        ans = []
        for i in range(len(freq)-1 ,0, -1):
            for num in freq[i]:
                ans.append(num)
            if len(ans) == k:
                break
        return ans