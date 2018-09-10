#!/usr/bin/env python
# coding: utf-8

def merge_sort(a, first = 0, last = None):
	"""
	Args:
		a: A list of unsorted items.
		first: The index of the first item.
		last: The index of the last item.
	
	Returns:
		A list of sorted items.
	
	Note:
		time: const * n * log_2(n)
	"""
	def merge_v_1(a, first, mid, last):
		left = a[first:mid + 1] + [float('Inf')]
		right = a[mid + 1:last + 1] + [float('Inf')]
		i = 0
		j = 0
		print 'L and R:', left, right
		for k in range(first, last + 1):
			if left[i] < right[j]:
				a[k] = left[i]
				i += 1
			else:
				a[k] = right[j]
				j += 1
		return a
	
	def merge_v_2(a, first, mid, last):
		left = a[first:mid + 1]
		right = a[mid + 1:last + 1]
		i = 0
		j = 0
		print 'L and R:', left, right
		for k in range(first, last + 1):
			if i < len(left) and j < len(right):
				if left[i] < right[j]:
					a[k] = left[i]
					i += 1
				else:
					a[k] = right[j]
					j += 1
			elif i < len(left):
				a[k] = left[i]
				i += 1
			elif j < len(right):
				a[k] = right[j]
				j += 1
		return a
	
	if last == None:
		last = len(a) - 1
	if not a or first == last:
		return a
	mid = (first + last) / 2
	merge_sort(a, first, mid)
	merge_sort(a, mid + 1, last)
	return merge_v_1(a, first, mid, last)


if __name__ == '__main__':
	print 'Input:', [5, 2, 4, 6, 1, 3, 5]
	print merge_sort([5, 2, 4, 6, 1, 3, 5])
