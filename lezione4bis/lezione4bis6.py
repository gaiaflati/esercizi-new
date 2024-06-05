def intersection(nums1: list[int], nums2: list[int]):
#nums1=[2,2,4,2,1]
#nums2=[1,1,2,0,2,1,2]
#return [1,2]
    nums3=[]
    for i in nums1:
        if i in nums2:
            nums3.append(i)
    print(set(nums3))
out=intersection([2,2,4,2,1],[1,1,2,0,2,1,2])
