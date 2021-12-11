def is_monotonic(nums1):
    if nums1 == sorted(nums1): 
        print (True)
    else:
        if nums1 == sorted(nums1, reverse=True): 
            print (True)
        else:
            print (False)
            

is_monotonic(nums)
