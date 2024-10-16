class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


    # def removeDuplicates(self, nums: List[int]) -> int:
    #     k = 0


    #     for i in range(len(nums)):
    #         for num in nums:
    #             if num == nums[i]:
    #                 k += k+1
    #                 print(num)
    #                 print("break")
        
    #     print(k)