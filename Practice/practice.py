#maximum occurence of sameelements
# arr = [1,2,2,3,4,4,4,5,5,5]
# maxcount = 0
# res = arr[0]
# current_count = 0
# for i in range(0,len(arr)):
#     current_count =0
#     for j in range(0,len(arr)):
#         if arr[i]==arr[j]:
#             current_count+=1
#     if current_count>maxcount:
#         maxcount=current_count
#         res=arr[i]
# print("maximum occurence element is:",res,"with count:",maxcount)

# sum of max and min element in array
# arr =[12,5,45,76,2,23,21]
# max=arr[0]
# min=arr[0]
# for i in range(len(arr)):
#     if arr[i]>max:
#         max=arr[i]
#     if arr[i]<min:
#         min=arr[i]
# print("sum of max and min element is:",max+min)

# calculate the sum and product of all elements in an array
# arr=[12,7,6,3]
# sum=0
# product=1
# for i in range(len(arr)):
#     sum=sum+arr[i]
#     product=product*arr[i]
# print("sum of all elements is:",sum)
# print("product of all elements is:",product)


#convert decimal to binary
# n=(int(input("Enter a Number: ")))
# binary=0
# x=1
# for i in range(0,32):
#     rem=n%2
#     binary=binary+rem*x
#     x=x*10
#     n=n//2
# print(binary)

#move zeros to end of array
# nums=[0,1,0,3,12]
# nonzero=0
# for i in range(0,len(nums)):
#     if nums[i]!=0:
#         nums[i],nums[nonzero]=nums[nonzero],nums[i]
#         nonzero+=1

# print(nums)

# count the number of even and odd elements in an array
# arr=[12,3,4,5,6,7,8,9]
# even_count=0
# odd_count=0
# for i in range(len(arr)):
#     if arr[i]%2==0:
#         even_count+=1 #     else:
#         odd_count+=1
# print("even count is:",even_count)
# print("odd count is:",odd_count)

# rotate array by k times
arr= [9,8,1,6,3]
lastvalue=arr[-1]
for i in range(len(arr)-1,-1,-1):
    arr[i]=arr[i-1]
arr[0]=lastvalue
print(arr)