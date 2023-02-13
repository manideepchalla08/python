def findpeakelemet(nums):
     strat,end=0,len(nums)-1
     while start<end:
         mid=(start+end)//2
         if nums[mid]>nums[mid+1]:
             end=mid
         else:
             start=mid+1
     return start
nums=[1,2,3,1]
print(findpeakelemet(nums))
