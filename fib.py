# the fibonacci sequence is as followed:

# 1, 1, 2, 3, 5, 8, 13, ...

# the first two numbers are 1 and 1. Then the next number is created from adding up the last two numbers.

# write a python function that takes in n as an argument (assume it's an integer) and returns n numbers of the fibonacci sequence.

# hint: you're returning a list, so you should initialize one in your method like this:

def fib(number):
	seq = [1, 1]

	if number == 0:
		return []
	elif number == 1:
		return [1]
	elif number == 2:
		return seq
	else:
		# number = 3 -> [1,1,2]
		for i in range(2, number): # this loop is going 3 times
			lastNum = seq[len(seq) - 1]
			secLastNum = seq[len(seq) - 2]
			seq.append(lastNum + secLastNum)
		return seq

print(fib(0)) # []

print(fib(2)) # [1, 1]

print(fib(90)) # [1, 1, 2, 3, 5, 8]

















