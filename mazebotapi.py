import numpy
import requests

def parse_maze(grid):
    """
    This function is called to parse the maze retrieved from MazebotAPI
    into numpy array format (class 'numpy.ndarray').
    """
    for array in grid:
        # print(array)
        index = 0
        for element in array:
            # print(element)
            if element == "X":
                array[index] = 1
            else:
                array[index] = 0
            index += 1
    
    return numpy.asarray(grid)


def get_mazebot_random():
    """
    Request and return a random size maze to MazebotAPI, including tuples
    with start and goal coordinates. Size may vary between 10, 20, 30, 40,
    60, 100, 120, 150, and 200. To restric range of possible sizes, call
    the function 'get_mazebot_sized' instead.
    """
    request_data = requests.get("https://api.noopschallenge.com/mazebot/random?minSize=10&maxSize=10").json()
    start = tuple(request_data["startingPosition"])
    goal = tuple(request_data["endingPosition"])
    raw_grid = request_data["map"]
    grid = parse_maze(raw_grid)

    return grid, start, goal


def get_mazebot_sized():
    """
    This function restricts the maze size retrieved from MazebotAPI by validating
    user input and parsing it into a valid request URL. MazebotAPI will generate a
    random maze of size inside the range you define via the inputs. Maximum size
    must be equal to or higher than minimum size, or MazebotAPI will respond with
    a 404 error. To get a maze of a specific size, set minimum and maximum as equal
    values.
    """

    def set_url():
        """
        This scoped function gets and validates user input to return a valid URL to be
        requested to MazebotAPI. Input validation is made using array of valid intgers,
        defined on the MazebotAPI documentation.
        """
        base_url = "https://api.noopschallenge.com/mazebot/random?minSize=''&maxSize=''"
        sizes = [10, 20, 40, 60, 100, 120, 150, 200]
        try:
            minSize = int(input("Please enter minimum array size. Valid values are: 10, 20, 40, 60, 100, 120, 150, and 200.\nType here: "))
            if minSize not in sizes:
                raise ValueError
            base_url = base_url.replace("minSize=''", "minSize={}".format(str(minSize)))

            maxSize = int(input("Please enter maximum array size. Valid values are: 10, 20, 40, 60, 100, 120, 150, and 200. Max size must be equal of higher than min size.\nType here: "))
            if minSize > maxSize or maxSize not in sizes:
                raise ValueError
            base_url = base_url.replace("maxSize=''", "maxSize={}".format(str(maxSize)))

            return base_url
        
        except ValueError:
            return print("Invalid input. Please enter a valid integer, and ensure that maximum maze size is equal to or higher than minimum size.")
    
    # Set URL with maze size constraints:
    base_url = set_url()

    # Get and parse maze data:
    request_data = requests.get(base_url).json()
    start = tuple(request_data["startingPosition"])
    goal = tuple(request_data["endingPosition"])
    raw_grid = request_data["map"]
    grid = parse_maze(raw_grid)

    return grid, start, goal
