"""
    Data una lista nums di interi, spostare gli zeri alla fine di questa lista
    mantenendo l'ordine originale dei numeri che non sono zeri

    Esempio 1:
    nums = [0,1,0,3,12] -> modificare la lista in [1,3,12,0,0]

    Esempio 2:
    nums= [0]-> la modifica è nulla
"""

def move_zeroes(nums: list[int]):
    for i in nums:
        if i==0:
            nums.remove(i)
            nums.append(i)
    print(nums)
out=move_zeroes([0,5,4,0,8,9])