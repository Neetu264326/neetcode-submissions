class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num = set(nums)
        longest = 0

        for i in num:
            if (i - 1) not in num:
                currentnum = i
                currentstreak = 1

                while (currentnum + 1) in num:
                    currentnum += 1
                    currentstreak += 1

                longest = max(longest, currentstreak)

        return longest