# A *

A * pathfinder algorithm experiments on a maze

- it started as a solver of a (at the time being) preset 
- there was a random maze function added

As part of Hacktoberfest 2019:
   <img src="https://hacktoberfest.digitalocean.com/assets/logo-hf19-header-8245176fe235ab5d942c7580778a914110fa06a23c3d55bf40e2d061809d8785.svg"  title="Hacktoberfest">


- @hangmansROP improved the style of the code by linting and code formatting
- @Fayhen has added functionality to get a maze from Github Mazebot
- @scavenger29 has added functionality to get the solved maze route from the algorithm transformed 
to the format Mazebot understands
- @tusharck9 has added the functionality to return a solved maze to Mazebot





### TLDR 

maze & start & end points:

<img src="https://github.com/mamonu/Astar/blob/master/mazestep_000.png"  title="maze">





### A* algorithm

In games we often want to find paths from one location to another. 
We’re not only trying to find the shortest distance; we also want to take into account travel time.

- Breadth First Search explores equally in all directions. 
    This is an incredibly useful algorithm, not only for regular path finding, 
    but also for procedural map generation, flow field pathfinding, distance maps, and other types of map analysis.


- Dijkstra’s Algorithm (also called Uniform Cost Search) lets us prioritize which paths to explore. 
    Instead of exploring all possible paths equally, it favors lower cost paths. 
    We can assign lower costs to encourage moving on roads, higher costs to avoid forests, 
    higher costs to discourage going near enemies, and more. 
    When movement costs vary, we use this instead of Breadth First Search.


- A* is a modification of Dijkstra’s Algorithm that is optimized for a single destination. 
    Dijkstra’s Algorithm can find paths to all locations; 
    A* finds paths to one location. It prioritizes paths that seem to be leading closer to the goal.






<img src="https://github.com/mamonu/Astar/blob/master/out.gif"  title="A*">





----

#### TODO/DONE:

 - create random maps with a function: DONE :v:   :game_die::game_die::game_die:

<img src="https://github.com/mamonu/Astar/blob/master/outrand.gif"  title="A*">


- use other distance metrics in the algorithm?

- integrate [MAZEBOT API](https://github.com/mamonu/Astar/blob/master/MazebotAPI.md)  : 
   
   * get a maze from the api  DONE :v:  
   * solve the maze DONE :v:  (this is what the algorithm does!)
   * function to return the solution through the API?  DONE :v:  
   * function to transform the path the algorithm outputs to the EWSN (for east/west/south/north) the Mazebot expects so it can be sent DONE :v:  
   
   
  
   

  




- use a graphics library to visualise everything in 3d: TODO :scream:
