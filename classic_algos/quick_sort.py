def quick_sort(lst):
	if not lst:
		return lst

	if len(lst) == 1:
		return lst

	pivot = lst[0]

	return quick_sort([x for x in lst if x < pivot]) + [x for x in lst if x == pivot] + quick_sort([x for x in lst  if x > pivot])

if __name__  == '__main__':
	assert quick_sort([8, 2, 1, 3, 1, 3]) == [1, 1, 2, 3, 3, 8]
	assert quick_sort([-1, 1, 1, 2, 1, 0.5]) == [-1, 0.5, 1, 1, 1, 2]
	print("All tests passed.")