def insertion_sort(array):
  length = len(array)
  if length <= 1:
    return array
  for i in range(1, length):
    flag = array[i]
    j = i- 1
    while j>=0 and array[j]>flag:
      array[j+1] = array[j]
      j -= 1
    array[j+1] = flag
  return array

test_array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
insertion_sort(test_array)
print(test_array)