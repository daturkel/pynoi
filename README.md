# pynoi
## A recursive solution to Towers of Hanoi implemented in python.

### Background

[Towers of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) is a puzzle where a stack of disks, decreasing in size from bottom to top, sit on one of three pegs and the player's objective is to move the stack to another peg without ever placing a larger disk on top of a smaller one. Only one piece can be moved at a time.

The implied challenge is not only to move the stack to a new peg but to do so in the lowest possible number of moves.

This gif from [Wikipedia](https://commons.wikimedia.org/wiki/File:Tower_of_Hanoi.gif) shows a minimal solution for a tower of three discs.

![](https://upload.wikimedia.org/wikipedia/commons/4/4f/Tower_of_Hanoi.gif)

(The gif was created by André Karwath and is made available under the [(CC BY-SA 2.5)](https://creativecommons.org/licenses/by-sa/2.5/deed.en) license.)

### Recursive approach

There are many ways to formulate the minimal solution to Towers of Hanoi, but the one I found easiest to implement was a recursive approach. We can think of the simplest nontrivial variant of the puzzle as the one with two discs, and the solution is such:

```
A: [2,1]
B: []
C: []

A->B (first move)
A: [2]
B: [1]
C: []

A->C (second move)
A: []
B: [1]
C: [2]

B->C (third move)
A: []
B: []
C: [2,1]
```

When we consider the three-disc variant, where we want to move three discs from A to C, we simply use the two disc solution to move the top two discs from A to B, then move the largest disc from A to C, and lastly use the two disc solution again to move the smaller two discs from B to C. Since the two-disc solution is three moves, this one is 3 + 1 + 3 = 7 moves. 

Applying this logic, a puzzle with n discs can always be solved by moving the top (n-1) discs from A to B, then moving the largest disc from A to C, and moving the top (n-1) discs again from B to C. This always takes 2x+1 steps, where x is the number of steps required to solve the puzzle with n-1 discs. As a result, the puzzle with n discs always takes (2^n)-1 moves.

Pynoi hard-codes the two-disc solution and then applies a the above recursive definition to solve the puzzle for any number of discs.

### In action

#### Initialize a new puzzle with 4 discs.
```python
from pynoi import TowersOfHanoi

puz = TowersOfHanoi(4)
print(puz)
```
```
[4, 3, 2, 1], [], []]
```

#### Automatically solve the puzzle.
(Verbose mode is default.)
```python
puz.solve()
```
```
1. (1,2): [[4, 3, 2], [1], []]
2. (1,3): [[4, 3], [1], [2]]
3. (2,3): [[4, 3], [], [2, 1]]
4. (1,2): [[4], [3], [2, 1]]
5. (3,1): [[4, 1], [3], [2]]
6. (3,2): [[4, 1], [3, 2], []]
7. (1,2): [[4], [3, 2, 1], []]
8. (1,3): [[], [3, 2, 1], [4]]
9. (2,3): [[], [3, 2], [4, 1]]
10. (2,1): [[2], [3], [4, 1]]
11. (3,1): [[2, 1], [3], [4]]
12. (2,3): [[2, 1], [], [4, 3]]
13. (1,2): [[2], [1], [4, 3]]
14. (1,3): [[], [1], [4, 3, 2]]
15. (2,3): [[], [], [4, 3, 2, 1]]
solved in 15 steps
```

Puzzle state is maintained.
```python
print(puz)
```
```
[4, 3, 2, 1], [], []]
```

#### Methods are exposed for manually manipulating the puzzle.
```python
puz.move(3,2)
```
```
(3,2): [[], [1], [4, 3, 2]]
```

```python
puz.reset()
print(puz)
```
```
[[], [], [4, 3, 2, 1]]
```

#### Illegal moves are forbidden.
The `TowersOfHanoi` object will not allow moves which start from an empty post or which move a bigger disc onto a smaller one. Successful moves return `True` and unsuccessful moves return `False`. This can be leveraged for implementing your own algorithm.

#### Verbose option.
Verbose mode can be disabled by instantiating the object with `verbose=False`:
```python
shh = TowersOfHanoi(5,verbose=False)
shh.solve()
```
```
[[], [], [5, 4, 3, 2, 1]]
solved in 31 steps
```

The object's `verbose` option can also be overridden by passing a boolean `verbose` argument to the `move()` or `solve()` methods.

#### Have fun!
```python
import time

big = TowersOfHanoi(24)

start = time.time()
big.solve(verbose=False)
end = time.time()

d = round(end - start,3)

print(f'and {d} seconds')
```
```
[[], [], [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
solved in 16777215 steps
and 21.579 seconds
```
