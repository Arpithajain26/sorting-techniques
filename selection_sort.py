def selectionsort(nums):


    for i in range(len(nums)-1):
        min=i
        for j in range(i+1,len(nums)-1):
            if nums[j]<nums[i]:
                min=j
        temp=nums[i]
        nums[i]=nums[min]
        nums[min]=temp
    return nums
a=selectionsort([2,3,1,4,5])
print(a)

