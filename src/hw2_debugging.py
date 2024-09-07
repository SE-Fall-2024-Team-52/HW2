"""
This module implements the merge sort algorithm.
"""
import rand


def merge_sort(input_arr):
    """
    Recursively sorts an array using the merge sort algorithm.

    Parameters:
    input_arr (list): The list to be sorted.

    Returns:
    list: A new sorted list.
    """
    if len(input_arr) <= 1:
        return input_arr

    half = len(input_arr) // 2

    return recombine(merge_sort(
        input_arr[:half]), merge_sort(input_arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into one sorted array.

    Parameters:
    left_arr (list): The first sorted list.
    right_arr (list): The second sorted list.

    Returns:
    list: A merged and sorted list.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    while right_index < len(right_arr):
        merge_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1

    while left_index < len(left_arr):
        merge_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1

    return merge_arr


if __name__ == '__main__':
    arr = rand.random_array([None] * 20)
    arr_out = merge_sort(arr)

    print(arr_out)
