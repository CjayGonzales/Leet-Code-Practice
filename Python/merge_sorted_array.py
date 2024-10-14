#create an array
nums1 = [4,2,3,2,1]
nums2 = [6,5,8,7,6]
result = []

n = 0
m = 0


for n in nums1:
    if n > 0:
        result.append(n)
        result.sort()
        print(result)

# was going to loop through and try to compare for each one and append it all to result but couldnt figure out how to compare each one
# this was the solution:

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         if n == 0 :return
#         len1 = len(nums1)
#         end_idx = len1-1
#         while n > 0 and m > 0 :
#             if nums2[n-1] >= nums1[m-1]:
#                 nums1[end_idx] = nums2[n-1]
#                 n-=1
#             else:
#                 nums1[end_idx] = nums1[m-1]
#                 m-=1
#             end_idx-=1
#         while n > 0:
#             nums1[end_idx] = nums2[n-1]
#             n-=1
#             end_idx-=1