class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 2 options, either linear with storing each element. Checking if current element has already been seen in our previous seen elements. So O(n) O(n).

        #OHHHHHHHHHH
        #The above solution is not O(n), as to see if current element is already in seen in worst case that is also O(n). So in total its actually O(n^2)
        # seen = []
        # for n in nums:
        #     if n in seen: return True
        #     seen.append(n)
        # return False

        #I could do a hashmap for O(1) lookup in the seen numbers
        seen = {}
        for n in nums:
            if n in seen: return True
            seen[n] = True
        return False
        
        #The other option is to first sort the array, then iterate through it, if we see any 2 elements are the same then we know there is a repeate. So a sort then iterate through. But here there would be no storing of element

        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
         
