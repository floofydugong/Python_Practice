'''

Given an int array length 2, return True if it contains a 2 or a 3.

has23([2, 5]) -> True
has23([4, 3]) -> True
has23([4, 5]) -> False

'''

def has23(nums):
    print (nums[0] in [2,3] or nums[1] in [2,3])

has23([1,1])