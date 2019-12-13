# Network-Simulation

todo list:
    [[[high priority]]]
    make nodes in a graph add other nodes that are within radius to their list of neighbors, probably in another method call to graph like "associateNeighbors()" or something

    [[[low priority]]]
    all classes:
        edge case:
            what if you gave them negative numbers for input parameters?
            solution:
                ignore it? this should all be internal so we shouldn't be giving them calls that don't make sense
                ***it'd look p good to be able to handle this in a 'nice' way though

    node class:
        edge case:
            what if trying to add nodes to empty graph with no base stations? (within range resolution would probably crash)

    graph class:

