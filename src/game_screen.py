from math import ged

def pgcd (nums):
    num1 = nums [0]
    for i in range (1,len (nums)):

        num1 = ged(num1, nums[i])

    return num1
nums = [15, 18, 20]

print (pgcd (nums))