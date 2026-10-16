class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        # space depends on algorithm
        nums.sort()

        # edgecase: one or no elements
        if (n == 1 or n == 0):
            return False

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True

        return False