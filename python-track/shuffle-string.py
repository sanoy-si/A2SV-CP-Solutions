class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [''] * len(s)
        
        for char, index in zip(s,indices):
            ans[index] = char
        
        return ''.join(ans)