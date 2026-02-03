# find out the maximum value in the array

# arr =[ 12,3,45,67,23,89,90]
# max=arr[0]
# for i in range(len(arr)):
#     if arr[i]>max:
#         max=arr[i]
# print("maximum value is:",max)

#find the second maximum value in the array
# import math
# arr=[12,7,8,6,9]
# max=-math.inf
# max2=-math.inf
# for cur in arr:
#     if cur>max:
#         max2=max
#         max=cur
#     elif cur > max2:
#         max2=cur
# print("second maximum value is:",max2)


#find the 2nd minimum value in the array
# import math
# arr=[12,7,8,6,9]
# min=math.inf
# min2=math.inf
# for cur in arr:
#     if cur<min:
#         min2=min
#         min=cur
#     elif cur < min2:
#         min2=cur
# print("second minimum value is:",min2)

# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(0,len(nums)):
#             firstnumber = nums[i]

#             for j in range(i,len(nums)):
#                 secondNumber =nums[j]
#                 if firstnumber+ secondNumber == target:
#                     return [i , j]