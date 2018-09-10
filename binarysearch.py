#!/usr/bin/env python
# coding: utf-8

def binary_search_cyclic(item, a):
	"""
	Args:
		item: The item being searched for.
		a: A list of items.
	
	Returns:
		The index of the item, None otherwise.
	"""
	first = 0
	last = len(a) - 1
	while first <= last:
		mid = (first + last) / 2
		if item == a[mid]:
			return mid
		elif item < a[mid]:
			last = mid
		elif item > a[mid]:
			first = mid + 1
	return None


def binary_search_recursive(item, a, first = 0, last = None):
	"""
	Args:
		item: The item being searched for.
		a: A list of items.
		first: The index of the first item.
		last: The index of the last item.
	
	Returns:
		The index of the item, None otherwise.
	"""
	if last == None:
		last = len(a) - 1
	mid = (first + last) / 2
	if not a or item != a[mid] and first == last:
		return None
	if item == a[mid]:
		return mid
	elif item < a[mid]:
		return binary_search_recursive(item, a, first, mid)
	elif item > a[mid]:
		return binary_search_recursive(item, a, mid + 1, last)


if __name__ == '__main__':
	print 'Search of 3 in [1, 2, 3, 4, 5, 5, 6]:', binary_search_cyclic(3, [1, 2, 3, 4, 5, 5, 6])
	print 'Search of 7 in [1, 2, 3, 4, 5, 5, 6]:', binary_search_cyclic(7, [1, 2, 3, 4, 5, 5, 6])
	print 'Search of 7 in [7]:', binary_search_cyclic(7, [7])
	print 'Search of 7 in []:', binary_search_cyclic(7, [])
	print 'Search of 3 in [1, 2, 3, 4, 5, 5, 6]:', binary_search_recursive(3, [1, 2, 3, 4, 5, 5, 6])
	print 'Search of 7 in [1, 2, 3, 4, 5, 5, 6]:', binary_search_recursive(7, [1, 2, 3, 4, 5, 5, 6])
	print 'Search of 7 in [7]:', binary_search_recursive(7, [7])
	print 'Search of 7 in []:', binary_search_recursive(7, [])
