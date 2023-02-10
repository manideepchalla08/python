def minjump(nums):
    jumps=0
    currnt_jump_end=0
    far=0
    for i in range(len(nums)-1):
        far=max(far,i+nums[i])
        if i==currnt_jump_end:
            jumps+=1
            current_jump_end=far
        return jumps
    
nums1=[1,3,5,8,9,6,7,8,9]
print(minjump(nums1))
