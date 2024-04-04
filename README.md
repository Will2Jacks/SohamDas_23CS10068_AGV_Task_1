The A Star Algorithm

The Initialise A Star function initialises the cost function of each cell. It is the Euclidean Distance of the cell from the source cell
The heuristic involves the Manhattan distance of the cell from the destination cell. It is just an estimation for the distance that remains to be travelled.

The set_parents is a stub function that calculates the parent of each cell. For the source cell the parent cell is itself. The role of this function is to store the parent of each cell in the
path as we go from the source to the destination

The calculateF function calculates the minimum f value for each cell, which is essentially the sum of the g and h values.This function keeps updating the f value of each cell as we go from 
the source to the destination

The find_neighbours function calculates the neighbours of each cell of the grid

