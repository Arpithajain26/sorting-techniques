class Solution:
    def bubbleSort(self, nums):
        def helper(n):
            if n==1:
                return 
            else:
                for i in range(n-1):
                    if nums[i]>nums[i+1]:
                        nums[i],nums[i+1]=nums[i+1],nums[i]
            helper(n-1)
        helper(len(nums))
        return nums
a=Solution()
x=a.bubbleSort([2,1,5,6,4,3,2])
print(x)
            
        