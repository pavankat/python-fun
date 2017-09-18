# 1. 

# make a variable called a, set it to 2

# make a variable called b, set it to 3

# add the variables together

a = 2
b = 3

print(a+b)

c = a+b
print(c)

# 2. 

# write a conditional statement that prints out hello if b is greater than a

# 3. 
# add an else to the previous conditional statement so that it prints bye if the first conditional is not met

if b > a:
	print("hello")
else:
	print("bye")

# 4. write a function that takes in a string argument
# and returns the string with the letter a added to it


def add_a(str):
	return str+"a"

def add_a(str):
	c = str + "a"
	return c

# optional
user_input = input('give me a word')
print(add_a(user_input))



# 3:03

# 5. how would you get the first element of a list named animals

animals[0]

# 6. how would you get the last element of a list named animals

animals[-1]
animals[len(animals)-1]

# 7. how would you get the 3rd element of a list named animals

animals[2]


# 8. initialize a variable named nums to a list
# and then loop from 1 to 5 and add each number to the nums list 
# then print out the nums 

# 3:13

nums = []
for i in range(1,6):
	nums.append(i)

print(nums)

# 9. write a function that takes in a string and reverses it and returns the reversed string
# dog -> god
# cat -> tac
# 3:23

def reverse_string(str):
	rev = ""

	for s in str:
		rev = s + rev

	return rev

def reverse_string(str):
	str_list = list(str)
	str_list.reverse()

	return ''.join(str_list)

def reverse_string(str):
	str_list = list(str)
	rev = str_list[::-1]

	return ''.join(rev)

print(reverse_string("dog")) #god
# rev = ""
# rev = "d" + ""
# rev = "d"
# rev = "o" + "d"
# rev = "od"
# rev = "g" + "od"
# rev = "god"

fibonacci: 1,1,2,3,5,8,13,21

write a function that takes a number and returns that many numbers in the fibonacci sequence


0 -> []
1 -> [1]
2 -> [1,1]
3 -> [1,1,2] -> 0th + 1st -> 2nd
4 -> [1,1,2,3] -> 1st + 2nd -> 3rd

def fib(n):
	fib_list = [1,1]

	if n==0:
		return []
	elif n==1:
		return [1]
	elif n== 2:
		return fib_list
	else:
		# do more here
		for i in range(2,n+1):
			next_num = fib_list[-1] + fib_list[-2]
			fib_list.append(next_num)
		return fib_list















