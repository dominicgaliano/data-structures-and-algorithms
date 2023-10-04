def mergeSort(lst):
    # base case
    if len(lst) < 2:
        return lst

    # divide
    lo, hi = 0, len(lst)
    mid = (hi - lo) // 2
    left, right = lst[:mid], lst[mid:]

    # sort recursively
    left, right = mergeSort(left), mergeSort(right)

    # combine
    left_i = 0
    right_i = 0

    result = []
    for _ in range(hi):
        # left smaller or right exhausted, add to result
        if (left_i < mid) and (
            (right_i >= hi - mid) or left[left_i] < right[right_i]
        ):
            result.append(left[left_i])
            left_i += 1
        # right smaller or left exhausted, add to result
        else:
            result.append(right[right_i])
            right_i += 1

    return result
