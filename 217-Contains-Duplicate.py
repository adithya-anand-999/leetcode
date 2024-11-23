class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        number = 0

        for n in nums:
            seen.add(n)
            number+=1
            if number != len(seen): return True
        return False