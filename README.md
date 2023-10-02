# Data Structures and Algorithms

I created this repository to practice my data structures and algorithms skills in Python.

## Data Structures

### Linked List

Sequential list of nodes that holds data which point to other nodes also containing data.

Usage:

- List, Queue, and Stack Implementation
- Circular Lists
- Can easily model real world objects like a train.
- Used in separate chaining, which is present in some hash table
  implementations to deal with hashing collisions.
- Often used for adjacency lists in graphs.

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

### Stack

One-ended linear data structure which models a real world stack by
having two primary operations, pop and push.

Usage:

- Used by undo mechanisms in text editors.
- Used in compiler syntax checking for matching brackets and braces.
- Used behind the scenes to support recursion by keeping track of previous function calls.
- Used for Depth First Search (DFS) graph traversal.

### Queue

Linear data structure which models real world queues by having two primary operations, namely enqueue and dequeue.

Usage:

- Any waiting line models a queue.
- Can be used to efficiently keep track of the x most recently added elements.
- Web server request management when you want first come first server.
- Breadth first search (BFS) graph traversal

| Operation | Time Complexity |
| --------- | --------------- |
| Enqueue   | O(1)            |
| Dequeue   | O(1)            |
| Peeking   | O(1)            |
| Contains  | O(n)            |
| Removal   | O(n)            |
| Is Empty  | O(1)            |

### Priority Queue

Abstract Data Type (ADT) that operates similar to a normal queue expect that each element has a certain priority. The priority of the elements in the priority queue determines the order in which elements are removed from the PQ.

Uses a heap. A heap is a tree based DS that satisfies the heap invariant (also called heap property): If A is a parent node of B then A is ordered with respect to B for all nodes A, B in the heap.

Usage:

- Used in certain implementations of Dijkstra's Shortest Path algorithm.
- Anytime you need to dynamically fetch the 'next best' or 'next worst' element.
- Used in Huffman coding (which is often used for lossless data compression).
- Best First Search (BFS) algorithms such as A\* use PQs to continuously grab the next most promising node.
- Used by Minimum Spanning Tree (MST) algorithms.

| Operation                                       | Time Complexity |
| ----------------------------------------------- | --------------- |
| Binary Heap Construction                        | O(n)            |
| Polling                                         | O(log(n))       |
| Peeking                                         | O(1)            |
| Adding                                          | O(log(n))       |
| Naive Removing                                  | O(n)            |
| Advanced removing with help from a hash table\* | O(log(n))       |
| Naive contains                                  | O(n)            |
| Contains check with help of a hash table\*      | O(1)            |

- Using a hash table to help optimize operations does take up linear space and also adds some overhead to the binary heap implementation.

## Algorithms

### Breadth First Search (BFS) Graph Traversal

Implemented using a queue.

```psuedocode
Let Q by a Queue
Q.enqueue(starting_node)
starting_node.visited = true

While Q in not empty Do

  node = Q.dequeue()

  For neighbor in neighbors(node):
    If neighbor has not been visited:
       neighbor.visited = true
       Q.enqueue(neighbor)
```
