

def find_constant_vars(data):
	zero_threshold = 1e-7

	columns = [[data[row][col] for row in xrange(len(data))] for col in xrange(len(data[0]))]

	max_values = [complexMax(columns[i]) for i in xrange(len(columns))]
	min_values = [complexMin(columns[i]) for i in xrange(len(columns))]

	difference = [getMagnitude(max_values[i] - min_values[i]) for i in xrange(len(max_values))]

	indices = [i for i in xrange(len(difference)) if (difference[i] > zero_threshold) ]
	return indices


def getMagnitude(complex_num):
	return (complex_num.real**2 + complex_num.imag**2)**.5

def complexMax(complex_nums):
	max_num = complex_nums[0]
	for i in xrange(len(complex_nums)):
		if getMagnitude(complex_nums[i]) > getMagnitude(max_num):
			max_num = complex_nums[i]
	return max_num


def complexMin(complex_nums):
	min_num = complex_nums[0]
	for i in xrange(len(complex_nums)):
		if getMagnitude(complex_nums[i]) < getMagnitude(min_num):
			min_num = complex_nums[i]
	return min_num