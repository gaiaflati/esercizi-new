"""
    Data una lista nums di n elementi, restituire l'elemento che
    compare più di n/2 volte

    Esempio:
    nums =[3,2,3]-> restituisce 3

    Esempio:
    nums = [2,2,1,1,1,2,2] -> restituisce 2
"""

def majority_element(nums: list[int]):
    for i in nums:
        if nums.count(i)> len(nums)/2:
            print(i)
            return i
    return None
out=majority_element([2,2,4,5,6,7,5,5])




   
   
   
   
   
   
   
