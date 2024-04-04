The A Star Algorithm

The Initialise A Star function initialises the cost function of each cell. It is the Euclidean Distance of the cell from the source cell
The heuristic involves the Manhattan distance of the cell from the destination cell. It is just an estimation for the distance that remains to be travelled.

The set_parents is a stub function that calculates the parent of each cell. For the source cell the parent cell is itself. The role of this function is to store the parent of each cell in the
path as we go from the source to the destination

The calculateF function calculates the minimum f value for each cell, which is essentially the sum of the g and h values.This function keeps updating the f value of each cell as we go from 
the source to the destination

The find_neighbours function calculates the neighbours of each cell of the grid

The AStar function initializes the open list with the starting node and an empty closed list.
It iterates until the destination is reached.
In each iteration:
It selects the node from the open list with the lowest f value.
Removes the selected node from the open list and adds it to the closed list.
If the selected node is the destination node, the function reconstructs the path using the parents array and returns it.
Otherwise, it expands the selected node by considering its neighbors, updating their costs (g) and f values if necessary, and adding them to the open list if they are not there already.

Once the AStar function completes its implementation,the parents array is looked into to reconstruct the path

The main function involves setting the start and the end nodes, the nodes which have obstacles(initialised with -1) and calling the AStar function.



The CBS(Conflict Based Search) Algorithm

The CBS Algorithm is implemented here. For simplicity only two agents have been considered.

This Node class represents a state 
It has attributes constraints, solution, and cost.
constraints: Stores the constraints imposed during the search at each step of the search.This ensures that there are no conflicts in the
solution
solution: Stores the solution paths for the agents,after ensuring no conflicts
cost: Represents the cost of the node.

The find_best_node function iterates through the list of nodes and returns the node with the lowest cost.

The set_first_path function computes the path for the first agent while considering constraints.
It utilizes the A* algorithm for the first agent, finds the path, and adjusts it according to the constraints.

The set_second_path function computes the path for the second agent while considering constraints.
It utilizes the A* algorithm for the second agent, finds the path, and adjusts it according to the constraints.

The main function initializes the search space, starting with an initial node representing no constraints.
It iteratively expands nodes until it finds a solution
If a solution is found, it prints the solution paths.

It alsoinitialises a maze/grid with obstacles.
It sets the starting and stopping points for two agents (start_rat1, start_rat2, stop_rat1, stop_rat2).
It begins the search process in the main1() function, where it iteratively explores nodes, considering constraints and updating the search space accordingly.
The search terminates when a valid solution is found
