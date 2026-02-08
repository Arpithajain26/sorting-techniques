def quicksort(nums,low,high):
    if low<high:

        partition=quick(nums,low,high)
        quicksort(nums,low,partition-1)
        quicksort(nums,partition+1,high)
def quick(nums,low,high):
    i=low
    pivot=nums[low]
    j=high
    while(i<j):
        while(nums[i]<=pivot and i<=high-1):
            i+=1
        while(nums[j]>pivot and j>=low+1):
            j-=1
        if(i<j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
    nums[low],nums[j]=nums[j],nums[low]
    return j
nums=[45,2,1,6,7,8,34,5]
a=quicksort(nums,0,len(nums)-1)
print(nums)
