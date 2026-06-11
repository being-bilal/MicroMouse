[[Projects]] [[Research]] [[Robotics]]

## Object 
Build a maze solving micromouse and test existing alogrithms to determine the best fit for the physical implementation. And improve the performance the existing algorithm experimentally for the research if possible.
## Simulation 
Before the implementation of the algorithms in the hardware, they are first implemented in simulation to test their accuracy and compare multiple algorithms to determine the fastest and the most accurate of all.
## Algorithms to Consider
* Basic Wall Follower Logic
* Dijstra's Shortest Path Algorithm
* Flood Fill method

#### WALL FOLLOWER LOGIC 
The most basic maze solving algorithm in which we simply just follow the left wall continuously until it leads to the centre. 
* Sense the left wall.
* If left wall present then flagl=1, if not then flagl=0.
* If flagl=1 then step 4 else turn left by 90 degrees.
* Sense the front wall.
* If front wall present then flagf=1, if not then flagf=0.
* if flagf=0, move straight else turn right by 90 degrees.
* return to step1.
The problem with this algorithm is that it can not be used to solve complex mazes that include a wall segment not connected to the outer boundary in its structure if that happens The mouse gets trapped in a loop around it forever. Other problems include lack of intelligence as it does not store the values of the maze in RAM and does not know when the maze is completed therefore even if it reaches the goal by luck, it can't do a fast speed run because it knows nothing about the maze structure. 

#### DIJKTRA ALGORITHM
Dijkstra's Algorithm is a shortest-path algorithm used to find the minimum-cost path from a starting node to all other nodes in a graph with non-negative edge weights. It is an offline algorithm i.e it requires entire maze to be represented as a graph of nodes with edges having equal or different weights before it can find the shortest path therefore before implementing the Dijstra's algorithm we have the mouse physically walks the entire maze to build a graph in the process called Traversal. Traversal can be done by random movements or by implementing depth first search that guarantees complete maze coverage. 
* The algorithm starts by assigning a distance of 0 to the source node and infinity to all other nodes.
* It then repeatedly selects the unvisited node with the smallest known distance, explores its neighbors, and updates their distances and assigns parents to them if a shorter path is found using the weights assigned to the edges.
* It continues until all nodes have been processed or the traget node is reached. Then it traverse back to the initial node using the parents of the nodes.
 problems in using this algorithm, the major one being that the whole maze has to be traversed. For identifying the nodes, it is important to travel all the parts of the maze, irrespective of whether that portion of the maze contains the shortest path or not.

#### Flood Fill Method
It is a online path finding algorithm that doesnt require intial traversal of the maze, it assign every cell a number representing its distance from the goal. The goal gets 0. The mouse always moves to the lowest numbered neighbor. It's walking downhill toward zero. The assignment of the numbers to the cell at the start is done by determine the manhattan distance where no walls are considered and each cell is given the value of the manhattan distance from the target position.
* The maze array = a 16×16 grid where each cell stores one number, its current best-known distance to the goal.

* The wall array = a separate structure storing every wall the mouse has physically discovered so far. 

* The temp[4] array = built fresh at every cell, stores the four neighbor values sorted ascending. This is the mouse's decision list at each ste

* **Search Run**
```
At every cell:
  1. Build temp[4] — sorted neighbor values
  2. Is temp[0] lower than current cell?
       NO  → cell value is wrong → correct it → correction 
             wave propagates outward → retry
       YES → valid downhill move exists
  3. Is target cell walled off?
       YES → try next candidate in temp[]
       NO  → move there
  4. Repeat until MAZE[R][C] = 0
```

* **Correction Wave**
	Triggered whenever a discovered wall makes a cell's value inconsistent. The rule every cell must satisfy:

```
my value = lowest accessible neighbor's value + 1
```

If this breaks, the cell updates itself and pushes its neighbors to check themselves. The wave propagates outward via a queue until all values are consistent again. Values only ever increase during correction so the wave always terminates.

* **Speed Run**
After reaching the goal and returning to start, the mouse has a much more complete wall map. One final re-flood with all known walls produces accurate distance values. Mouse runs at full speed following the gradient, no stopping to sense.