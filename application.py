from node import Node
from baseStation import BaseStation
from graph import Graph
from cmd import Cmd

class MyPrompt(Cmd):

    currentGraph = Graph(100,100)
    source = -1
    destination = -1

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit

    def do_start(self, args):
        """Takes 4 inputs: number of base stations, number of nodes, radius of base station, radius of nodes\n(Example: start 2 10 40 25)
        """
        l = args.split()
        if len(l) != 4:
            print ("Invalid number of arguments.")
            return
        else:
            self.currentGraph = Graph(100,100)
            self.currentGraph.addBases(int(l[0]), int(l[2]))
            self.currentGraph.addNodes(int(l[1]), int(l[3]))
            self.currentGraph.addNeighbors()
            #self.currentGraph.printGraph()

    def do_printgraph(self, args):
        """Prints the graph onto the terminal"""
        self.currentGraph.printGraph()

    def do_source(self, args):
        """Takes one input, the node id, e.g. "source 5"
        """
        self.source = int(args)

    def do_destination(self, args):
        """Takes one input, the node id, e.g. "destination 5"
        """
        self.destination = int(args)

    def do_route(self, args):
        """Reports whether a route was found between the source and destination set earlier, and gives path.
        """
        self.currentGraph.getRoute(self.source, self.destination) 

    def do_scramble(self, args):
        """Scrambles the positions of all the nodes except for the set source and destination.\n
        Note: source and destination need to be set for this command to not crash the program."""
        self.currentGraph.scramble(self.source, self.destination)


if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = 'Type help to get availalbe commands\n> '
    prompt.cmdloop('Welcome to the mesh network simulation (simple).')