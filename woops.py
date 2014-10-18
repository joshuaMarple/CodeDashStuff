import fileinput, sys

#rules

def rule1(numstr):
	return ('7' in numstr)

def rule2(numstr):
	return(int(numstr) % 7 == 0)

def rule3(numstr):
	base=0
	for char in numstr:
		base += int(char)
	return (base == 7)

#players

def playerCheck(prev, numstr, name):
	if name == 'Richard':
		return richardCheck(prev, numstr)
	elif name == 'Michael':
		return michaelCheck(prev, numstr)
	elif name == 'Tim':
		return timCheck(prev, numstr)
	elif name == 'Lyndsey':
		return lyndseyCheck(prev, numstr)
	elif name == 'JR':
		return JRCheck(prev, numstr)
	else: 
		return correctCheck(prev, numstr)

def correctCheck(prev, numstr):
	if rule1(numstr) or rule2(numstr) or rule3(numstr):
		return 'Whoops!'
	else:
		return str(int(numstr))

def richardCheck(prev, numstr):
	if prev == 'Whoops!':
		return ''
	elif rule1(numstr) or rule2(numstr) or rule3(numstr):
		return 'Whoops!'
	else:
		return str(int(numstr))

def michaelCheck(prev, numstr):
	if rule2(numstr) or rule3(numstr):
		return 'Whoops!'
	else:
		return str(int(numstr))

def timCheck(prev, numstr):
	if rule1(numstr) or rule3(numstr):
		return 'Whoops!'
	else:
		return str(int(numstr))

def lyndseyCheck(prev, numstr):
	if rule2(numstr) or rule1(numstr):
		return 'Whoops!'
	else:
		return str(int(numstr))

def JRCheck(prev, numstr):
	return str(int(numstr))

#playerRules = {"Richard" : richardCheck, "Michael" : michaelCheck, "Tim" : timCheck, "Lyndsey" : lyndseyCheck, "JR" : JRCheck}

def main():

	#Input stuff (might want to change to array of chars)
	lines=[]
	deli = fileinput.input()
	for line in deli:
		#char array
		#linelist = []
		#for char in line:
		#	linelist.append(char)
		#lines.append(linelist)
		#word array
		lines.append(line.split())


	#actual stuff

	names = []
	rounds = []

	for x in range(0,len(lines)):
		if x % 2 == 0:
			names.append(lines[x])
		else:
			rounds.append(lines[x])

	
	# for each game
	for x in range(0, len(names)):
		#make a list to hold the scores
		errors = []
		for n in range(0,len(names[x])):
			errors.append(0)
		#reset some values for the game
		direction = 1
		index = 0
		eor_count = 0
		roundnum = int(rounds[x][0])
		prev = ''
		value = '1'
		#for each round
		for y in range(0,roundnum):
			#value and prev resets but player index does not.
			prev = ''
			value = '1'
			#as long as we keep getting the right answer:
			while  playerCheck(prev, value, names[x][index]) == correctCheck(prev, value):
				#print(index)
				#print the answer
				print(names[x][index] + '-' + correctCheck(prev, value))
				#reverse direction if necessarry
				if correctCheck(prev, value) == 'Whoops!':
					if 1 == direction:
						direction = -1
					else:
						direction = 1
				#make sure prev is right
				prev = correctCheck(prev, value)
				#increment value
				value = str(int(value)+1)

				#increment the index by direction and check that it is within bounds
				index += direction
				if index >= len(names[x]):
					index = 0
				if index < 0:
					index = len(names[x]) - 1
				#print(index)
			#-----------------------------
			#when we get a wrong answer:

			#print it out
			print(names[x][index] + '-' + playerCheck(prev, value, names[x][index]))
			#print END OF ROUND
			print('END OF ROUND')
			#add one to the appropriate player's score
			errors[index] += 1
			reverse direction, but do not change index
			if 1 == direction:
				direction = -1
			else:
				direction = 1
		#------------------------------------------------------------
		#at the end of each game, print the scores for each player and then --
		for y in range(0,len(names[x])):
			print(names[x][y] + ': ' + str(errors[y]))
		print("--")




		#
		#while True:
		#	#for a recognized name
		#	if names[x][index] in playerRules:
		#		correctValue = correctCheck(prev, value)
		#		if playerRules[names[x][index]](prev, value) == correctValue:
		#			print(names[x][index], correctValue)
		#			if correctValue ==  'Whoops!':
		#				prev = 'Whoops!'
		#			else: 
		#				prev = ''
		#			value = str(int(value)+1)
#



	#while(eor_count < tot_eor):
	# print(lines)






	

if __name__ == "__main__":
    main()
