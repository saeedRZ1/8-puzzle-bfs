#!/usr/bin/env python3
"""
8-Puzzle solver (BFS)

Usage examples:
    # default start state (simple)
    python3 bfs_puzzle_8.py

    # specify start state (9 integers 0..8). 0 is the blank.
    python3 bfs_puzzle_8.py --start 1 2 3 4 0 5 6 7 8

    # change goal state or max nodes explored
    python3 bfs_puzzle_8.py --goal 1 2 3 4 5 6 7 8 0 --max-nodes 100000
"""
from collections import deque
import argparse
import time

NEIGHBORS = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def bfs(start, goal, max_nodes=200000):
    """
    Breadth-first search for 8-puzzle.
    start, goal: lists of length 9 containing numbers 0..8 (0 is blank).
    Returns (path, nodes_explored) where path is list of states from start to goal (inclusive).
    """
    start_t = tuple(start)
    goal_t = tuple(goal)
    queue = deque([(start_t, [start_t])])
    visited = {start_t}
    nodes = 0

    while queue:
        state, path = queue.popleft()
        nodes += 1

        if state == goal_t:
            # convert tuples back to lists
            return [list(s) for s in path], nodes

        if nodes > max_nodes:
            return None, nodes

        zero = state.index(0)
        for n in NEIGHBORS[zero]:
            new_state = list(state)
            new_state[zero], new_state[n] = new_state[n], new_state[zero]
            t_state = tuple(new_state)
            if t_state not in visited:
                visited.add(t_state)
                queue.append((t_state, path + [t_state]))

    return None, nodes

def pretty_print(state):
    """Print a 3x3 state nicely (state is a list of 9 ints)."""
    print(f"{state[0]} {state[1]} {state[2]}")
    print(f"{state[3]} {state[4]} {state[5]}")
    print(f"{state[6]} {state[7]} {state[8]}")

def parse_args():
    p = argparse.ArgumentParser(description="8-puzzle BFS solver")
    p.add_argument('--start', nargs=9, type=int, help='start state (9 ints 0..8)')
    p.add_argument('--goal', nargs=9, type=int, default=[1,2,3,4,5,6,7,8,0], help='goal state (default: 1..8,0)')
    p.add_argument('--max-nodes', type=int, default=200000, help='max nodes to explore (safety limit)')
    return p.parse_args()

def main():
    args = parse_args()
    start = args.start if args.start else [1,2,3,4,0,5,6,7,8]
    goal = args.goal

    print("Start:", start)
    print("Goal :", goal)
    t0 = time.time()
    path, nodes = bfs(start, goal, max_nodes=args.max_nodes)
    t1 = time.time()

    if path is None:
        print(f"No solution found (explored {nodes} nodes) — try increasing --max-nodes or a different start.")
        print(f"Time: {t1-t0:.2f}s")
        return

    moves = len(path) - 1
    print(f"\nSolved in {moves} moves. Explored {nodes} nodes. Time {t1-t0:.2f}s\n")
    for i, s in enumerate(path):
        print(f"Step {i}:")
        pretty_print(s)
        print("---")

if __name__ == '__main__':
    main()
