# just a simple binary search algorthm Python 3.12

def binarySearchHelper(lst, elt, left, right):
    
    if left > right:
        return None
    else:
        mid = (left + right) // 2

        if lst[mid] == elt:
            return  mid
        
        elif lst[mid] < elt:
            return  binarySearchHelper(lst, elt, mid + 1, right)
        else:
            return  binarySearchHelper(lst, elt, left, mid - 1)


def binarySearch(lst, elt):
    index = binarySearchHelper(lst, elt, 0, len(lst) - 1)
    if index is not None:
        print("Element found at index:", index)
    else:
        print("Element not found")


if __name__ == "__main__":
    
    lst = [1, 6, 7, 14, 17, 21, 25]
    elt = 17

    binarySearch(lst, elt)