# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python/656b74a489b24aad94c5eaaf


def move_zeros(lst):
    for num in lst:
        if num == 0:
            lst.remove(num)
            lst.append(0)
    return lst