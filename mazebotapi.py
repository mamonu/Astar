import numpy as np
import requests
import json


def parse_maze(grid):

    # This  function  is  called  to  parse  the  maze  retrieved  from  MazebotAPI
    # into  numpy  array  format  (class  'np.ndarray').

    for array in grid:
        index = 0
        for element in array:
            if element == "X":
                array[index] = 1
            else:
                array[index] = 0
            index += 1

    return np.asarray(grid)


def get_mazebot_random():

    #   Request  and  return  a  random  size  maze  to  MazebotAPI,  including  tuples
    #   with  start  and  goal  coordinates.  Size  may  vary  between  10,  20,  30,  40,
    #   60,  100,  120,  150,  and  200.  To  restric  range  of  possible  sizes,  call
    #   the  function  'get_mazebot_sized'  instead.

    request_data = requests.get(
        "https://api.noopschallenge.com/mazebot/random?min_size=10&max_size=10"
    ).json()
    start = tuple(request_data["startingPosition"])
    goal = tuple(request_data["endingPosition"])
    maze_path = request_data["mazePath"]
    raw_grid = request_data["map"]
    grid = parse_maze(raw_grid)

    return maze_path, grid, start, goal


def return_solution(maze_path, directions):

    #   Get  the  maze  id  from  the  get  maze  function  and  return  it  from  this  function.
    #   "mazePath":  "/mazebot/mazes/dTXurZOonsCbWC9_PDBWpiRAvBME3VBDIf9hcwwCdNc"
    #   The  above  key  is  to  be  used  to  do  the  same
    #

    payload = {"directions": directions}
    request_data = requests.post(
        "https://api.noopschallenge.com/" + maze_path, data=json.dumps(payload)
    ).json()

    if "success" in request_data["result"]:
        print("Message:  ", request_data["message"])
        print("Shortes  Solution  Length:  ", request_data["shortestSolutionLength"])
        print("Bot  Solution  Length:  ", request_data["yourSolutionLength"])

    else:
        print(request_data["message"])


def get_mazebot_sized():

    #   This  function  restricts  the  maze  size  retrieved  from  MazebotAPI  by  validating
    #   user  input  and  parsing  it  into  a  valid  request  URL.  MazebotAPI  will  generate  a
    #   random  maze  of  size  inside  the  range  you  define  via  the  inputs.  Maximum  size
    #   must  be  equal  to  or  higher  than  minimum  size,  or  MazebotAPI  will  respond  with
    #   a  404  error.  To  get  a  maze  of  a  specific  size,  set  minimum  and  maximum  as  equal
    #   values.

    def set_url():

        #     This  scoped  function  gets  and  validates  user  input  to  return  a  valid  URL  to  be
        #     requested  to  MazebotAPI.  Input  validation  is  made  using  array  of  valid  intgers,
        #     defined  on  the  MazebotAPI  documentation.

        base_url = (
            "https://api.noopschallenge.com/mazebot/random?min_size=''&max_size=''"
        )
        sizes = [10, 20, 40, 60, 100, 120, 150, 200]
        try:
            min_size = int(
                input(
                    "Please  enter  minimum  array  size.  Valid  values  are:  10,  20,  40,  60,  100,  120,  150,  and  200.\nType  here:  "
                )
            )
            if min_size not in sizes:
                raise ValueError
            base_url = base_url.replace(
                "min_size=''", "min_size={}".format(str(min_size))
            )

            max_size = int(
                input(
                    "Please  enter  maximum  array  size.  Valid  values  are:  10,  20,  40,  60,  100,  120,  150,  and  200.  Max  size  must  be  equal  of  higher  than  min  size.\nType  here:  "
                )
            )
            if min_size > max_size or max_size not in sizes:
                raise ValueError
            base_url = base_url.replace(
                "max_size=''", "max_size={}".format(str(max_size))
            )

            return base_url

        except ValueError:
            return print(
                "Invalid  input.  Please  enter  a  valid  integer,  and  ensure  that  maximum  maze  size  is  equal  to  or  higher  than  minimum  size."
            )

    #  Set  URL  with  maze  size  constraints:
    base_url = set_url()

    #  Get  and  parse  maze  data:
    request_data = requests.get(base_url).json()
    start = tuple(request_data["startingPosition"])
    goal = tuple(request_data["endingPosition"])
    raw_grid = request_data["map"]
    maze_path = request_data["mazePath"]
    grid = parse_maze(raw_grid)

    return maze_path, grid, start, goal
