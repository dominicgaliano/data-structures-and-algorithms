def quickSort(lst):
    """Inplace sorting of array using quick sort algorithm"""
    if len(lst) == 0:
        return []
    quickSortHelper(0, len(lst) - 1, lst)


def quickSortHelper(lo, hi, lst):
    """
    Merge sort helper function.

        Parameters:
            lo (int): Starting index of sort range
            hi (int): Ending index of sort range (inclusive)
            lst (list): List to be sorted on

        Returns:
            lst (str): List with values sorted
    """
    if lo >= hi:
        return

    # determine pivot (also places pivot at hi)
    pivot = createPivot(lo, hi, lst)

    i = lo
    j = lo
    while j < hi:
        # Compare all elements to pivot.
        # If element is larger than pivot, leave in place
        # If element is smaller than pivot, swap then increment i
        # This pushes all elements smaller than pivot to the left
        # and leaves us with being the new location for pivot
        if lst[j] <= pivot:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1

        j += 1

    # put pivot in correct location
    lst[i], lst[hi] = lst[hi], lst[i]

    # recursively sort subarrays
    quickSortHelper(lo, i - 1, lst)
    quickSortHelper(i + 1, hi, lst)


def createPivot(lo, hi, lst):
    """Determine pivot using median-of-three method and place it at index 'hi'"""
    mid = (lo + hi) // 2
    if lst[mid] < lst[lo]:
        lst[lo], lst[mid] = lst[mid], lst[lo]
    if lst[hi] < lst[lo]:
        lst[lo], lst[hi] = lst[hi], lst[lo]
    if lst[mid] < lst[hi]:
        lst[mid], lst[hi] = lst[hi], lst[mid]
    pivot = lst[hi]
    return pivot
