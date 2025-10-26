def quicksort(arr, low, high):
  """
  Recursively sorts an array using the quicksort algorithm
  Args:
    arr: The array to be sorted
    low: Starting index of the partition
    high: Ending index of the partition
  """
  if low < high:
    # Find the partition index and sort the elements around it
    pi = partition(arr, low, high)
    # Recursively sort the left partition
    quicksort(arr, low, pi)
    # Recursively sort the right partition
    quicksort(arr, pi + 1, high)

def partition(arr, low, high):
  """
  Partitions the array around a pivot element
  Args:
    arr: The array to be partitioned
    low: Starting index of the partition
    high: Ending index of the partition
  Returns:
    The final position of the pivot element
  """
  # Choose the first element as pivot
  pivot = arr[low]
  i = low - 1
  j = high + 1

  while True:
    # Find element on left that is >= pivot
    i += 1
    while arr[i] < pivot:
      i += 1

    # Find element on right that is <= pivot
    j -= 1
    while arr[j] > pivot:
      j -= 1

    # If pointers meet or cross, return partition point
    if i >= j:
      return j

    # Swap elements at i and j
    arr[i], arr[j] = arr[j], arr[i]


# Example usage
if __name__ == "__main__":
  # Test array
  arr = [10, 7, 8, 9, 1, 5]
  n = len(arr)
  # Sort the array using quicksort
  quicksort(arr, 0, n - 1)
  print("Sorted array is:", arr)
