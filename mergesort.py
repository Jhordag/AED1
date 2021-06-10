
import time

def merge(left, right):
	result = [] 
	x, y = 0, 0
	for k in range(0, len(left) + len(right)):
		if x == len(left): 
			result.append(right[y]) 
			y += 1
		elif y == len(right): 
			result.append(left[x]) 
			x += 1
		elif right[y] < left[x]:
			result.append(right[y])
			y += 1
		else:
			result.append(left[x])
			x += 1
	return result

def mergesort(ar_list):
	length = len(ar_list)
	size = 1
	while size < length:
		size+=size 
		for pos in range(0, length, size):
			start = pos
			mid  = pos + int(size / 2)
			end = pos + size
			left = ar_list[ start : mid ] 
			right = ar_list[ mid : end ] 
			ar_list[start:end] = merge(left, right)
	return ar_list





