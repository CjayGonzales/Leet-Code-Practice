class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # getting the modulo of k
        k = k % len(nums)

        # setting pointers and reverse entire array
        l, r = 0, len(nums)-1

        # first while loop reverses
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]

            # increment and decrement pointers
            l, r = l+1, r-1

        # reverse the first "k" element
        l, r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        
        # reverse the rest of the array
        l, r = k, len(nums) - 1 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1