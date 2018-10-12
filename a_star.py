import numpy as np
import heapq
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


# maze grid in numpy array format. TODO : create random mazes with a function

grid = np.array([
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


## with the following code, a random maze grid is created.
#  
#   randomgrid = np.random.randint(2, size=(SIZE,SIZE))
#   however not all mazes are solvable. needs more work
#   perhaps whats needed is not so much random as procedural.
#   or random and then perturbed...
######

def randomgrid(mazesize):
    grid = np.random.randint(0,2, size=(mazesize,mazesize))
    solution = np.random.randint(1,2, size=(mazesize,mazesize))
    lasti = 0 #starting on left in x plane
    lastj = 0 #starting on top  in y plane
    i = 1
    while(i>0):
        solution[lasti, lastj] = 0
        grid[lasti, lastj] = 0
        if((lasti == mazesize-1) and (lastj == mazesize-1)): #stoping when we find the exit at bottom right corner of the maze
            rounds = i
            i = -1
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
        i += 1
    if(rounds >= mazesize*mazesize): #thus we make sure we don't get very "clear" pathway
        return randomgrid(mazesize)
    print(solution)
    return grid

# taking manhattan distance as the A* heuristic. TODO : try more distances as A* heuristics

def heuristic(a, b):
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

def eukleidian(a,b):
	dim = len(a)	# dimention of vector a
	c = 0			# declaring variable for storing a^2 + b^2
	while(dim>0):   # loop with iterations=dimention for S(a^2+b^2)
		c += ((b[dim-1] - a[dim-1]) ** 2) #dim-1 because of the a[0],b[0]
		dim -= 1
	return np.sqrt(c)

def britishrl(a,b):
	dim = len(a)
	c1 = 0
	c2 = 0
	while(dim>0):
		c1 += np.sqrt((b[dim - 1]) ** 2) #the oldschool way of abs 
		c2 += np.sqrt((a[dim - 1]) ** 2)
		dim -= 1
	return c1 + c2

def rsm(a,b): 	# radar screen metric 
	dim = len(a)
	aminb = a
	while(dim>0):
		aminb[dim-1] = abs(b[dim - 1] - a[dim-1])    
		dim -= 1
	aminb.append(1)
	min_aminband1 = min(aminb)
	return min_aminband1
	
def astar(array, start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))
    
    while oheap:

        current = heapq.heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
                
    return False




start = (0,0)
goal = (19,19)


route = astar(grid, start, goal)
route = route + [start]
route = route[::-1]



#extract x and y coordinates from route list
x_coords = []
y_coords = []


for i in (range(0,len(route))):
    with plt.xkcd():
        x = route[i][0]
        y = route[i][1]
        x_coords.append(x)
        y_coords.append(y)
        fig, ax = plt.subplots(figsize=(8,8))
        ax.imshow(grid, cmap=plt.cm.Dark2)
        ax.scatter(start[1],start[0], marker = "*", color = "yellow", s = 200)
        ax.scatter(goal[1],goal[0], marker = "+", color = "red", s = 200)
        ax.plot(y_coords,x_coords, color = "black")
        plt.xticks([])
        plt.yticks([])
        plt.title("A* algorithm step "+str(i))

        ##output numbering in a ffmpeg compatible way!

        if (i<10):
            filename = "mazestep_00%d.png" % i
        elif (i>9)&(i<100):
            filename = "mazestep_0%d.png" % i
        else:
            filename = "mazestep_%d.png" % i

        
        plt.savefig(filename)
        plt.close()
    #plt.show()
    
    
 


 # need to then run from the shell: 
 # ffmpeg -v warning -i mazestep_%03d.png -y out.gif
