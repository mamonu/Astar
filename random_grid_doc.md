In the following procedure's code we will make a random maze of given size and on it randomly clear a path one step at a time setting off in a random starting position on one of the maze's four borders. Solution's path will also be stored in a "solution" matrix (same size of course with our maze's matrix). The path will be cleared one step at a time, in random movementes in the i,j (x,j) plane. Hope that's clear!

def randomgrid(mazesize): 
	grid = np.random.randint(0,2, size=(mazesize,mazesize))

randomizing initial maze of size (mazesize)

	solution = np.random.randint(1,2, size=(mazesize,mazesize))

defining solution cheat-maze that will eventually store the maze's random-generated solution

	starting_border = np.random.randint(0,4)
	if(starting_border == 0):
		lasti = np.random.randint(0,mazesize)
		lastj = 0
	elif(starting_border == 1):
		lasti = np.random.randint(0,mazesize)
		lastj = mazesize - 1
	elif(starting_border == 2):
		lasti = 0
		lastj = np.random.randint(0,mazesize)
	elif(starting_border == 3):
		lasti = mazesize - 1
		lastj = np.random.randint(0,mazesize)

lasti, lastj will store the current steps on the maze's solution pathway. The code above selects the border that will be the starting position of the path. e.g. if the first if is the case, the starting position will be in the left border of the maze (with random i and j=0).

	i = 1
	while(i>0):

we set i equal to 1 and enter a loop which will stop when i inherits the value of 0 or less (i is an integer, classic selection for a pointer in a loop). We arbitarilly set i equal to i+1 in the end of this while loop so that we achieve the loop to continue looping plus having a measure of how much the path has procceded, something we will use in 2 lines of code below, where we select the case that will give the i a value that will exit the while=loop, only if i is formerly big enough (so that bigger solution=paths are to be achieved, though it's not a _strickt_ measurement of paths lenght or complexity)
		
		solution[lasti, lastj] = 0

as we mentioned before, lasti-lastj store the paths current position in the maze. here we achieve "creating" the path in the solution - matrix, so that we will showcase it in the end of the function. This way we achieve visualising the solution created by the function.
		
		grid[lasti, lastj] = 0

Here we also set the random-generated-matrix to have the same path as the solution's, thus achieving our firstly random generated map will have at least one randomly generated solution to it. By comparing A_star.py's pathway to solution's pathway we can come to some interesting considerations about the quality of our pathfinding code.

		if(((lasti == 0) or (lasti == mazesize-1) or (lastj == mazesize-1) or (lastj == 0)) and i>14):  # setting param i bigger will result in bigger labyrinth paths : ) 
			i = -1

here we set the while's exit case. If we are in a border, and we have made at least 14 steps (including going "forwards and backwards")
the while loop will break. We arbitarilly set i to be equal to -1 so that with the i++ in the end of the in-loop code the i will eventually equal zeros and the loop will exit in the check i greater than 0 (i>0).

		stepi = 0
		stepj = 0
		while(stepi==0 and stepj==0):
			if(lasti == 0):
				stepi += np.random.randint(0,2)
				lasti = lasti + stepi
			elif(lasti == mazesize - 1):
				stepi -= np.random.randint(0,2)
				lasti = lasti + stepi
			elif(lasti > 0 and lasti < (mazesize-1)):
				stepi = np.random.randint(0,2)
				addminuscase = np.random.randint(0,2)			
				if (addminuscase==0): 
					lasti = lasti + stepi			
				else:
					lasti = lasti - stepi

stepi,j are the steps the solution's path will follow on the maze. we initially set them to zeros and enter a loop that will exit when at least on of them take a random positive or negative 1 value and then gets added to the current pathway (lasti). If we formerely where in a border (thus lasti would be equal to zero or mazesize-1) we only make forward/only make backward movement on the path, with each case done in it's respective proper procedure. If we are not on a border (thus lasti > 0 and lasti < (mazesize-1)) we make a random movement of 1 step towhards ehter positive (if(addminuscase==0)) or negative(else:) direction. We also may stand still if stepi=0, though we can't stand still in both i and j axis because we are in the while(stepi==0 and stepj==0) loop, that will exit if and only if stepi or stepj (or even both) gets the value of 1, thus we will make a move on the i plane.

			if(lastj == 0):
				stepj += np.random.randint(0,2)
				lastj = lastj + stepj
			elif(lastj == mazesize - 1):
				stepj -= np.random.randint(0,2)
				lastj = lastj + stepj			
			elif(lastj > 0 and lastj < (mazesize-1)):
				stepj = np.random.randint(0,2)
				addminuscase = np.random.randint(0,2)
				if (addminuscase==0): 
					lastj = lastj + stepj
				else:
					lastj=lastj - stepj

same as above procedure for the j plane.

		i += 1

the i ascends a value of 1 thus creating our "step memmory" and insuring that the first while loop will continue looping

	print(solution)

we print the solution matrix, wich will showcase zeros in the solution's path and ones everywhere else.

	return grid

the function returns the grid maze, which is the firstly random generated maze (of 1 - obstacles/walls and 0 - free path).

73's