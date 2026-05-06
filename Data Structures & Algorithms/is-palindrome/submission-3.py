class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        s = re.sub(r"\s+", "", s)
        rs = s[::-1]
        return s == rs