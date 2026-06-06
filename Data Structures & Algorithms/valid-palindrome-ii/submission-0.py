class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check(left, right, deleted):

         
            if left >= right:
                return True

            if s[left] == s[right]:
                return check(left + 1, right - 1, deleted)

        
            if deleted:
                return False

        
            return (
                check(left + 1, right, True) or
                check(left, right - 1, True)
            )

        return check(0, len(s) - 1, False)