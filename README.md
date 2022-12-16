# Min Conflicts CSP [CSE 140]
Solves the constraint satisfaction problem outlined below.    
## The problem
Suppose you are given a linear graph that has nodes of the following colors:
```
Red
Yellow
Green
Blue
Violet
```
Each node has a domain of {1, 2, ..., 9}.    

Each node type has the following constraints on its value:    
```
Red - No contraints
Yellow - equals the rightmost digit of of the product of all its neighbors
Green - equals the rightmost digit of the sum of all its neighbors
Blue - equals the leftmost digit of the sum of all its neighbors
Violet - equals the leftmost digit of the product of all of its neighbors
```

## The program
The python file MinConflictsCSP.py contains my implementation of the solver function as well as 4 test cases (given to us in class to test our code). 
