def bubblesort(nums):
    n=len(nums)
    for i in range(n-1,1,-1):
        for j in range(0,i+1):
            if nums[i]<nums[j]:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
    return nums
a=bubblesort([5,3,1,23,56])
print(a)

