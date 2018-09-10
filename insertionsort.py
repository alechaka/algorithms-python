#!/usr/bin/env python
# coding: utf-8

def insertion_sort(a):
	"""
	Args:
		a: A list of unsorted items.
	
	Returns:
		A list of sorted items.
	
	Note:
		time: const * squared(n)
		memory: n
	"""
	for j in range(1, len(a)):
		item = a[j]
		i = j - 1
		while i > -1 and a[i] > item:
			a[i + 1] = a[i]
			i -= 1
		a[i + 1] = item
		print 'Step {}:'.format(j), a
	return a


if __name__ == '__main__':
	print 'Input:', [5, 2, 4, 6, 1, 3, 5]
	print insertion_sort([5, 2, 4, 6, 1, 3, 5])
