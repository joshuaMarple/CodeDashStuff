import fileinput, sys


def builder(input, iter, max):
	if (iter != max):
		build = ""
		prevdig = input[0]
		num_count = 0
		for dig in input:
			if dig == prevdig:
				num_count+=1
			else:
				build += str(num_count) + prevdig
				num_count = 1
				prevdig = dig
		if (num_count > 0):
			build += str(num_count) + prevdig
		print(build)
		builder(build, iter+1, max)
	else: 
		return None

lines=[]
file = fileinput.input()
# for line in file:
	#char array
	#linelist = []
	#for char in line:
	#	linelist.append(char)
	#lines.append(linelist)
	#word array
	# lines.append(line.split())

builder("313", 0, 10)


