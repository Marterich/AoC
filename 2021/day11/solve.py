#! /usr/bin/env python3
def read_file(filename):
	return [[[int(pos),0] for pos in line.strip()] for line in open(filename,"r").readlines()]
flash_counter = 0
def solve(grid):
	def flash_octopus(i_line, i_pos):
		global flash_counter
		flash_counter += 1
		# Set the flash the octopus to have flashed
		grid[i_line][i_pos][1] = 1
		# Reset the energy of the octopus
		grid[i_line][i_pos][0] = 0

		# Increase energy of surrouding octopuses
		if i_line == 0:
			#Check Left top Corner
			if i_pos == 0:
				grid[i_line][i_pos+1][0] 	+= 1	# increase right
				grid[i_line+1][i_pos+1][0] 	+= 1 	# increase right below
				grid[i_line+1][i_pos][0] 	+= 1	# increse below
			#Check Right Top Corner
			elif i_pos == len(grid[i_line])-1:
				grid[i_line][i_pos-1][0] 	+= 1 	# increase left
				grid[i_line+1][i_pos-1][0] 	+= 1 	# increase left below
				grid[i_line+1][i_pos][0]	+= 1 	# increase below
			#Check top row
			else:
				grid[i_line][i_pos+1][0] 	+= 1 	# increase right
				grid[i_line+1][i_pos+1][0] 	+= 1 	# increase right below
				grid[i_line][i_pos-1][0] 	+= 1 	# increase left
				grid[i_line+1][i_pos-1][0] 	+= 1 	# increase left below
				grid[i_line+1][i_pos][0]	+= 1 	# increase below

		elif i_line == len(grid)-1:
			#Check Left bottom Corner
			if i_pos == 0:
				grid[i_line][i_pos+1][0] 	+= 1	# increase right
				grid[i_line-1][i_pos+1][0] 	+= 1 	# increase right above
				grid[i_line-1][i_pos][0] 	+= 1	# increse above				
			#Check right bottom Corner
			elif i_pos == len(grid[i_line])-1:
				grid[i_line][i_pos-1][0] 	+= 1 	# increase left
				grid[i_line-1][i_pos-1][0] 	+= 1 	# increase left above
				grid[i_line-1][i_pos][0]	+= 1 	# increase above
			#Check bottom row
			else:
				grid[i_line][i_pos+1][0] 	+= 1 	# increase right
				grid[i_line-1][i_pos+1][0] 	+= 1 	# increase right above
				grid[i_line][i_pos-1][0] 	+= 1 	# increase left
				grid[i_line-1][i_pos-1][0] 	+= 1 	# increase left above
				grid[i_line-1][i_pos][0]	+= 1 	# increase above
		#Check left side
		if i_pos == 0 and i_line != 0 and i_line != len(grid)-1:
			grid[i_line-1][i_pos][0] 	+= 1	# increse above
			grid[i_line-1][i_pos+1][0] 	+= 1 	# increase right above
			grid[i_line][i_pos+1][0] 	+= 1 	# increase right
			grid[i_line+1][i_pos+1][0] 	+= 1 	# increase right below
			grid[i_line+1][i_pos][0]	+= 1 	# increase below
		#Check right side
		elif i_pos == len(grid[i_line])-1 and i_line != 0 and i_line != len(grid)-1:
			grid[i_line-1][i_pos][0] 	+= 1	# increse above
			grid[i_line-1][i_pos-1][0] 	+= 1 	# increase left above
			grid[i_line][i_pos-1][0] 	+= 1 	# increase left
			grid[i_line+1][i_pos-1][0] 	+= 1 	# increase left below
			grid[i_line+1][i_pos][0]	+= 1 	# increase below

		#Check everything else
		if i_line != 0 and i_line != len(grid)-1 and i_pos != 0 and i_pos != len(grid[i_line])-1:
			grid[i_line-1][i_pos][0] 	+= 1	# increse above
			grid[i_line-1][i_pos+1][0] 	+= 1 	# increase right above
			grid[i_line][i_pos+1][0] 	+= 1 	# increase right
			grid[i_line+1][i_pos+1][0] 	+= 1 	# increase right below
			grid[i_line+1][i_pos][0]	+= 1 	# increase below
			grid[i_line+1][i_pos-1][0] 	+= 1 	# increase left below
			grid[i_line][i_pos-1][0] 	+= 1 	# increase left
			grid[i_line-1][i_pos-1][0] 	+= 1 	# increase left above

		# Check for any new flashes
		for i_line in range(len(grid)):
			for i_pos in range(len(grid[i_line])):
				if grid[i_line][i_pos][0] > 9:
					flash_octopus(i_line,i_pos)	
		# Reset energy of octopuses which have flashed already
		for i_line in range(len(grid)):
			for i_pos in range(len(grid[i_line])):
				if grid[i_line][i_pos][1] == 1:
					grid[i_line][i_pos][0] = 0
			
	def check_grid():
			# iterate through each octopus. If it hasnt flashed already, increment it's energy by one and check if it is ready to flash
			for i_line in range(len(grid)):
				for i_pos in range(len(grid[i_line])):
					if grid[i_line][i_pos][1] == 0:
						grid[i_line][i_pos][0] += 1
					# check energy level
					if grid[i_line][i_pos][0] > 9 and grid[i_line][i_pos][1]==0:
						flash_octopus(i_line,i_pos)

	def reset_count_flash():
		# check if every octopus has flashed. If yes, return true. At the same time reset every flash indicator
		octopus_count  = len(grid)*len(grid[0])
		for i_line in range(len(grid)):
			for i_pos in range(len(grid[i_line])):
				if grid[i_line][i_pos][1] == 1:
					octopus_count -= 1
				grid[i_line][i_pos][1] = 0
		if octopus_count == 0:
			return True
		return False
	step = 0
	while True:
		if reset_count_flash():
			break
		check_grid()
		if step == 100:
			flashes_at_100 = flash_counter
		step += 1
	return flashes_at_100, step

result = solve(read_file("input.txt"))
print("PartI: ", result[0])
print("PartII:", result[1])
