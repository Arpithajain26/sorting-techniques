"""def mergesort(arr,low,high):
    if(low>=high):
        return
    else:
        mid=(low+high)//2
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)
def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while(left<=mid and right<=high):
        if(arr[left]<arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
    return arr
arr=[3,1,67,54,23,41,90,57,1,2,3,4,34]
a=mergesort(arr,0,len(arr)-1)
print(arr)

"""

class Solution:
    def mergeSort(self, nums):
        return self.merge(nums,0,len(nums)-1)
    
    def mergesortreal(self,nums,low,mid,high):
        temp=[]
        left=low
        right=mid+1
        while(left<=mid and right<=high):
            if(nums[left]<nums[right]):
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while(left<=mid):
            temp.append(nums[left])
            left+=1
        while(right<=high):
            temp.append(nums[right])
            right+=1
        for i in range(low,high+1):
            nums[i]=temp[i-low]
        return nums
    def merge(self,nums,low,high):
        if(low>=high):
            return
        else:
            mid=(low+high)//2
            self.merge(nums,low,mid)
            self.merge(nums,mid+1,high)
            self.mergesortreal(nums,low,mid,high)
a=Solution()
nums=[1,678,43,24,32,4,6,2,3]
a.mergeSort(nums)
print(nums)

        