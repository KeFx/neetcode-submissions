class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared_numbers = []
        for n in nums:
            if n not in appeared_numbers:
                appeared_numbers.append(n)
            else:
                return True
        return False