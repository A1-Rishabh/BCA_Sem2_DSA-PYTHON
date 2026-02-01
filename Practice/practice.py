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
n=(int(input("Enter a Number: ")))
binary=0
x=1
for i in range(0,32):
    rem=n%2
    binary=binary+rem*x
    x=x*10
    n=n//2
print(binary)