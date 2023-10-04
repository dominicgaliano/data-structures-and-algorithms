# inplace, william fiset version
def mergeSort(lst):
    if len(lst) == 0:
        return []
    return mergeSortHelper(0, len(lst) - 1, lst)


def mergeSortHelper(lo, hi, lst):
    """
    Merge sort helper function.

        Parameters:
            lo (int): Starting index of sort range
            hi (int): Ending index of sort range (inclusive)
            lst (list): List to be sorted on

        Returns:
            lst (str): List with values sorted
    """
    # base case, one element
    if lo == hi:
        return [lst[lo]]

    # divide
    mid = (lo + hi) // 2

    # sort recursively
    left = mergeSortHelper(lo, mid, lst)
    right = mergeSortHelper(mid + 1, hi, lst)

    # combine
    return merge(left, right)


def merge(left, right):
    result = []
    l, r = 0, 0

    while l != len(left) or r != len(right):
        if l == len(left):
            result.append(right[r])
            r += 1
        elif r == len(right):
            result.append(left[l])
            l += 1
        elif left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    return result


# my version, creates new list
# def mergeSort(lst):
#     # base case
#     if len(lst) < 2:
#         return lst

#     # divide
#     lo, hi = 0, len(lst)
#     mid = (hi - lo) // 2
#     left, right = lst[:mid], lst[mid:]

#     # sort recursively
#     left, right = mergeSort(left), mergeSort(right)

#     # combine
#     left_i = 0
#     right_i = 0

#     result = []
#     for _ in range(hi):
#         # left smaller or right exhausted, add to result
#         if (left_i < mid) and (
#             (right_i >= hi - mid) or left[left_i] < right[right_i]
#         ):
#             result.append(left[left_i])
#             left_i += 1
#         # right smaller or left exhausted, add to result
#         else:
#             result.append(right[right_i])
#             right_i += 1

#     return result
