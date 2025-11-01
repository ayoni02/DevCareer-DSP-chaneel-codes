class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = []
        for i in range(len(s)):
            res.append(s[indices.index(i)])
        return "".join(res)
