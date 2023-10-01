# Data Structures and Algorithms

I created this repository to practice my data structures and algorithms skills in Python.

## Linked List

Sequential list of nodes that holds data which point to other nodes also containing data.

Usage:

- List, Queue, and Stack Implementation
- Circular Lists
- Can easily model real world objects like a train
- Used in separate chaining, which is present in some hash table
  implementations to deal with hashing collisions
- Often used for adjacency lists in graphs

Types:

- Singly Linked
  - Pros:
    - Uses Less Memory
    - Simpler implementation
  - Cons:
    - Cannot easily access previous elements
- Doubly Linked
  - Pros:
    - Can be traversed backward
  - Cons:
    - Takes 2x memory

## Stack

One-ended linear data structure which models a real world stack by
having two primary operations, pop and push.

Usage:

- Used by undo mechanisms in text editors
- Used in compiler syntax checking for matching brackets and braces
- Used behind the scenes to support recursion by keeping track of previous function calls.
- Used for Depth First Search (DFS)
