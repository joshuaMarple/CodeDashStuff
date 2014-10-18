import fileinput, sys
import math
# grid = [["u"]
grid = ["1001",
"1000",
"1000",
"1100",
"0101",
"0001",
"0000",
"0100",
"0001",
"0000",
"0000",
"0100",
"0011",
"0010",
"0010",
"0110"]
# print(grid)

width = int(math.sqrt(len(grid)))

goal = 7
loc = 0
for i in grid:
	new_val = []
	for j in range(0, 4):
		if i[j] == "0":
			if j == 0:
				new_val.append("u")
			elif j == 1:
				new_val.append("r")
			elif j == 2:
				new_val.append("d")
			elif j == 3:
				new_val.append("l")
	grid[loc] = new_val
	loc += 1

# print(grid)


def run(pos, dir, hist):
	# print(pos)
	# print(dir)
	# print(hist)
	# print(grid[pos])
	# print("===============")
	if (pos, dir) in hist:
		# print("path not found")
		ans.append(False)
		return None
	if dir in grid[pos]:
		if dir == "u":
			pos -= width
		elif dir == "d":
			pos += width
		elif dir == "l":
			pos -= 1
		elif dir == "r":
			pos += 1

		run(pos, dir, hist)
	else:
		if pos == goal:
			# print("path found")
			ans.append(True)
			return None
		hist.append((pos, dir))
		# ans = []
		for direction in grid[pos]:
			run(pos, direction, hist)
		# return True in ans

ans = []
run(4, "u", [])
run(4, "d", [])
if True in ans:
	print("path found")
else:
	print("path not found")