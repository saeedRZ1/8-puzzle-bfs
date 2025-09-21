# 8-Puzzle Solver (BFS)

A simple 8-puzzle solver implemented with **Breadth-First Search (BFS)** in Python.

## Description
This project contains a small command-line program that solves the 8-puzzle (3x3 sliding puzzle) using BFS.  
The blank tile is represented by `0`.

The solver is intentionally simple (BFS) to demonstrate search, visited-state handling and path reconstruction.  
For harder start states you may need A* (with Manhattan distance) or other heuristics — BFS can blow up combinatorially.

## Files
- `bfs_puzzle_8.py` — the solver script (no external dependencies).

## How to run
```bash
# default simple start state
python3 bfs_puzzle_8.py

# supply a custom start state (9 integers, 0 is the blank)
python3 bfs_puzzle_8.py --start 1 2 3 4 0 5 6 7 8

# change the goal or increase the exploration limit
python3 bfs_puzzle_8.py --goal 1 2 3 4 5 6 7 8 0 --max-nodes 100000
```

## Output
The program prints the start and goal, then the number of moves and each intermediate state (3x3) step by step.

## Notes / Future improvements
- Replace BFS with A* search + Manhattan distance for performance.
- Add move labels (Up/Down/Left/Right) instead of states.
- Add unit tests and a small web/GUI demo with Pygame.
- Add a script to verify solvability of a start state (parity check).

## License
MIT
