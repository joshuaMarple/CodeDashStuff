import fileinput, sys

def main():

	#Input stuff (might want to change to array of chars)
	lines=[]
	deli = fileinput.input()
	for line in deli:
		#char array
		linelist = []
		for char in line:
			linelist.append(char)
		lines.append(linelist)
		#word array
		#lines.append(line.split(' '))



	#actual stuff
	print(lines)


	

if __name__ == "__main__":
    main()
