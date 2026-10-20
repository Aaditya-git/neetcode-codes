class Solution:
    def isHappy(self, n: int) -> bool:

        def get_square(n):
            ans = 0
            while n>0:
                rem = n % 10
                ans += rem * rem
                n = n // 10
            return ans

        duplicate = set()

        while n!=1 and n not in duplicate:
            duplicate.add(n)
            n = get_square(n)

        if n == 1:
            return True
        else:
            return False
        