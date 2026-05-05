from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        result = [0] * n

        # Bước 1: Tính mảng prefix (Tích các số phía trước index i)
        # Bắt đầu từ index 1 vì index 0 không có phần tử nào bên trái
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Bước 2: Tính mảng suffix (Tích các số phía sau index i)
        # Bắt đầu từ phần tử áp chót (n-2) đi ngược về 0
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Bước 3: Tính kết quả bằng cách nhân prefix và suffix tương ứng
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result
        
