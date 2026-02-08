def swap(nums,i,j):
    temp=nums[i]
    nums[i]=nums[j]
    nums[j]=temp
def insertionsort(nums):
    for i in range(len(nums)):
        j=i
        while (j>0 and nums[j-1]>nums[j]):
            swap(nums,j-1,j)
            j-=1
    return nums
a=insertionsort([2,1,5,6,4,3,2])
print(a)