class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        checkerSet = set()

        for num in nums:
            if num in checkerSet:
                return True
            else:
                checkerSet.add(num)

        return False