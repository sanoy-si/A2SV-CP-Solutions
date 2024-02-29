class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        curr = 0

        left = 1
        right = 2 ** (n - 1)

        for _ in range(n - 1):
            mid = (left + right) // 2

            if k <= mid:
                right = mid

            else:
                left = mid + 1
                curr = 1 if not curr else 0 

        return curr