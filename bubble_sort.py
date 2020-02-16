def bubble_sort(array):
  length = len(array)
  if length <= 1:
    return array
  for i in range(length):
    swap_flag = False
    for j in range(length - i - 1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]
        swap_flag = True
    if not swap_flag:
      break
  return array

test_array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
bubble_sort(test_array)
print(test_array)