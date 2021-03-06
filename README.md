# MulticriteriaShortestPathsProblem
In this paper a pathfinding problem is analyzed starting from a classical shortest path problem and then, after several optimization, going to resolve a graph that utilizes two static weights on its arcs, considering the most full satisfying set of solutions.

As well known, Dijkstra’s algorithm is the most widely used to solve
routing problems; in fact is very easy to create an implementation that attempts to find the best path in a classical weighted graph. So the paper will focus on the operations of optimization. The main part of the paper is the one that analyzes the paths of a graph with two weights for each arc, one value represents the distance (also present in the mono-criteria problem) and the other represents the danger of that arc. So the implementation will not only find the shortest and safest path, but also all the paths (not dominated) that take intermediate values.
