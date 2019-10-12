import heapq
import numpy
import matplotlib.pyplot as plt
import mazebotapi  # To import MazebotAPI request functions from mazebotapi.py


grid = numpy.array(
    [
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
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)


def random_grid(maze_size):
    """Generate a random maze grid.
        random_grid = numpy.random.randint(2, size=(SIZE,SIZE))
        Note: Not all mazes are currently solvable.
        TODO: Look into procedural generation over random"""
    grid = numpy.random.randint(0, 2, size=(maze_size, maze_size))
    solution = numpy.random.randint(1, 2, size=(maze_size, maze_size))
    x_plane = 0  # starting on left in x plane
    y_plane = 0  # starting on top  in y plane
    i = 1
    while i > 0:
        solution[x_plane, y_plane] = 0
        grid[x_plane, y_plane] = 0
        if (x_plane == maze_size - 1) and (y_plane == maze_size - 1):
            rounds = i
            i = -1
        x_step = 0
        y_step = 0
        while x_step == 0 and y_step == 0:
            if x_plane == 0:
                x_step += numpy.random.randint(0, 2)
                x_plane = x_plane + x_step
            elif x_plane == maze_size - 1:
                x_step -= numpy.random.randint(0, 2)
                x_plane = x_plane + x_step
            elif x_plane > 0 < (maze_size - 1):
                x_step = numpy.random.randint(0, 2)
                addminuscase = numpy.random.randint(0, 2)
                if addminuscase == 0:
                    x_plane = x_plane + x_step
                else:
                    x_plane = x_plane - x_step
            if y_plane == 0:
                y_step += numpy.random.randint(0, 2)
                y_plane = y_plane + y_step
            elif y_plane == maze_size - 1:
                y_step -= numpy.random.randint(0, 2)
                y_plane = y_plane + y_step
            elif y_plane > 0 < (maze_size - 1):
                y_step = numpy.random.randint(0, 2)
                addminuscase = numpy.random.randint(0, 2)
                if addminuscase == 0:
                    y_plane = y_plane + y_step
                else:
                    y_plane = y_plane - y_step
        i += 1
    if rounds >= maze_size * maze_size:
        return random_grid(maze_size)
    print(solution)
    return grid


def heuristic(vector_a, vector_b):
    """ Taking manhattan distance as the A* heuristic.
        TODO : try more distances as A* heuristics."""
    return numpy.sqrt(
        (vector_b[0] - vector_a[0]) ** 2 + (vector_b[1] - vector_a[1]) ** 2
    )


def eukleidian(vector_a, vector_b):
    dimension = len(vector_a)  # dimension of vector a
    result = 0  # declaring variable for storing a^2 + b^2
    while dimension > 0:  # loop with iterations=dimension for S(a^2+b^2)
        result += (
            vector_b[dimension - 1] - vector_a[dimension - 1]
        ) ** 2  # dimension-1 because of the a[0],b[0]
        dimension -= 1
    return numpy.sqrt(result)


def britishrl(vector_a, vector_b):
    dimension = len(vector_a)
    i = 0
    y = 0
    while dimension > 0:
        i += numpy.sqrt((vector_b[dimension - 1]) ** 2)  # the oldschool way of abs
        y += numpy.sqrt((vector_a[dimension - 1]) ** 2)
        dimension -= 1
    return i + y


def radar_screen_metric(vector_a, vector_b):
    # radar screen metric
    dimension = len(vector_a)
    aminb = vector_a
    while dimension > 0:
        aminb[dimension - 1] = abs(vector_b[dimension - 1] - vector_a[dimension - 1])
        dimension -= 1
    aminb.append(1)
    return min(aminb)


def astar(array, start, goal):

    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    close_set = set()
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    o_heap = []

    heapq.heappush(o_heap, (f_score[start], start))

    while o_heap:

        current = heapq.heappop(o_heap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = g_score[current] + heuristic(current, neighbor)
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

            if neighbor in close_set and tentative_g_score >= g_score.get(neighbor, 0):
                continue

            if tentative_g_score < g_score.get(neighbor, 0) or neighbor not in [
                i[1] for i in o_heap
            ]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(o_heap, (f_score[neighbor], neighbor))

    return False


start = (0, 0)
goal = (19, 19)

# Uncomment line below if you wish to run the script with a random maze from MazebotAPI
# In case of TypeError, rerun script and try again
# maze_path, grid, start, goal = mazebotapi.get_mazebot_random()

# Uncomment line below if you wish to run the script with a random maze within defined size constraints
# In case of TypeError, rerun script and try again
# maze_path, grid, start, goal = mazebotapi.get_mazebot_sized()

route = astar(grid, start, goal)
route = route + [start]
route = route[::-1]


# extract x and y coordinates from route list
x_coords = []
y_coords = []


for i, item in enumerate(route):
    with plt.xkcd():
        x = route[i][0]
        y = route[i][1]
        x_coords.append(x)
        y_coords.append(y)
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(grid, cmap=plt.cm.Dark2)
        ax.scatter(start[1], start[0], marker="*", color="yellow", s=200)
        ax.scatter(goal[1], goal[0], marker="+", color="red", s=200)
        ax.plot(y_coords, x_coords, color="black")
        plt.xticks([])
        plt.yticks([])
        plt.title("A* algorithm step " + str(i))

        # Output numbering in a ffmpeg compatible way!
        if i < 10:
            filename = "mazestep_00%d.png" % i
        elif (i > 9) & (i < 100):
            filename = "mazestep_0%d.png" % i
        else:
            filename = "mazestep_%d.png" % i

        plt.savefig(filename)
        plt.close()
    # plt.show()


# need to then run from the shell:
# ffmpeg -v warning -i mazestep_%03d.png -y out.gif
