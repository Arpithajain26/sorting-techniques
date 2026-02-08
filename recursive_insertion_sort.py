class Solution:
    def insertionSort(self, nums):
        def helper(n):
            if n==1:
                return 
            helper(n-1)
            j=n-1
            while j>0 and nums[j-1]>nums[j]:
                nums[j-1],nums[j]=nums[j],nums[j-1]
                j-=1
        helper(len(nums)) 
        return nums
a=Solution()
x=a.insertionSort([2,1,5,6,4,3,2])
print(x)
    