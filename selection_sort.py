def selectionsort(nums):


    for i in range(len(nums)-1):
        min=i
        for j in range(i,len(nums)-1):
            if nums[j]<nums[min]:
                min=j
        temp=nums[i]
        nums[i]=nums[min]
        nums[min]=temp
    return nums
a=selectionsort( [7, 4, 1, 5, 3])
print(a)

"""class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums)):
            min=i
            for j in range(i,len(nums)):
                if nums[i]>nums[j]:
                    min=j
            temp=nums[i]
            nums[i]=nums[min]
            nums[min]=temp
        return nums
a=Solution()
x=a.selectionSort( [7, 4, 1, 5, 3])
print(x)"""