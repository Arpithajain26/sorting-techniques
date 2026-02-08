def bubblesort(nums):
    n=len(nums)
    for i in range(n-1,0,-1):
        for j in range(0,i+1):
            if nums[i]<nums[j]:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
    return nums
a=bubblesort([4,2, 6, 8, 9])
print(a)

