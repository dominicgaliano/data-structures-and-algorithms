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

Using a hash table to help optimize operations does take up linear space and also adds some overhead to the binary heap implementation.

#### Binary Heap:

- Binary Heap is a binary tree that supports the heap invariant. In a binary tree every node has exactly two children.
- A complete binary tree is a tree in which at every level, except possible the last is completely filled and all the nodes are as far left as possible.
- Binary Heap Representation can be represented using an array (fast) or pointer-node model.

- For array representation:
  - let i be the parent node index.
  - left child index: 2i + 1
  - right child index: 2i + 2
  - (zero based)
- Adding Elements to Binary Heap
  - Add element to end of heap
  - "Bubble-up" until heap invariant is satisfied
- Removing Root elements from Binary Heap
  - Always want to remove the root, it's called polling and no searching is required.
  - Replace root with element at end of binary heap
  - "Bubble-down" by swapping with smaller child (for min heap) (left child in case of tie) until heap invariant satisfied.
- Naive removal from Binary Heap
  - Scan linearly for desired element
  - Remove and swap with element at end of binary heap
  - "Bubble-up" or "Bubble-down" as necessary to satisfy heap invariant.
- Removing Elements from Binary Heap in O(log(n))
  - Using Hashtable to lookup where the node is indexed at (constant time)
  - Caveat (what if there are two or more nodes with the same value or hash)?
    - Instead of mapping one value to one position, we will map one value to multiple positions
    - We can maintain a set or tree set of indexes for which a particular node value (key) maps to.
    - Have to track movement of nodes during bubble-up and bubble-down in the index tree.

### Disjoint Set (Union Find)

- Union find is a data structure that keeps track of elements which are split into one or more disjoint sets.
- It has two primary operations: find and union.

Usage:

- Kruskal's minimum spanning tree algorithm
- Grid percolation
- Network Connectivity
- Least common ancestor in trees
- Image processing

| Operation          | Complexity |
| ------------------ | ---------- |
| Construction       | O(n)       |
| Union              | α(n)       |
| Find               | α(n)       |
| Get component size | α(n)       |
| Check if connected | α(n)       |
| Count components   | O(1)       |

α(n) = amortized constant time

Creation:

- First construct a **bijection** (a mapping) between your objects and integers in the range [0, n).
  - Not necessary in general, but will allow us to construct an array-based union find.
- Find operation:
  - To find which component a particular element belongs to, find the root of that component by following the parents nodes until a self loop is reached (a node who's parent node is itself).
- Union operation:
  - To unify two elements, find which are the root nodes for each component and if the root nodes are different make one of the root nodes be the parent of the other.

### Binary Trees (BT) and Binary Search Trees (BST)

- A tree is an undirected graph which satisfies any of the following:

  - An acyclic connected graph.
  - A connected graph with N nodes and N-1 edges.
  - A graph in which any two vertices are connected by _exactly_ one path.

- A binary tree is a tree in which every node has at most two children.
- A binary search tree is a binary tree that satisfies the BST invariant:
  - Left tree has smaller elements, right tree has larger elements

Usage:

- BST:
  - Implementation of some map and set ADTs
  - Red Black Trees
  - AVL Trees
  - Splay Trees
  - etc.
- Used in the implementation of of binary heaps
- Syntax trees (used by compilers and calculators)
- Treap - a probabilistic DS (uses a randomized BST)

BST:

| Operation | Avg       | Worst |
| --------- | --------- | ----- |
| Insert    | O(log(n)) | O(n)  |
| Delete    | O(log(n)) | O(n)  |
| Remove    | O(log(n)) | O(n)  |
| Search    | O(log(n)) | O(n)  |

Adding elements to a BST:

- compare new element to root
- recurse down left tree (< case)
- recurse down right tree (> case)
- handle finding a duplicate value (= case)
- create a new node (found a null leaf)

Removing elements from BST:

1. Find the element we wish to remove (if it exists)
2. Replace the node we want to remove with it's successor (if any) to maintain BST invariant.

- 4 removal cases:
  - Node to remove is leaf node
    - Can easily just remove
  - Node to remove has only left subtree
    - Left subtree becomes new successor of node's parent
  - Node to remove has only right subtree
    - Right subtree becomes new successor of node's parent
  - Node to remove has both left and right subtree
    - Successor can either be the largest value of the left subtree or smallest value of the right subtree

Traversal

- preorder

  - prints before recursive calls

  ```pseudocode
  preorder(node):
    if node == null: Return
    print(node.value)
    preorder(node.left)
    preorder(node.right)
  ```

- inorder

  - prints between recursive calls

  ```pseudocode
  inorder(node):
    if node == null: Return
    print(node.value)
    inorder(node.left)
    inorder(node.right)
  ```

- postorder

  - prints after recursive calls

  ```pseudocode
  postorder(node):
  if node == null: Return
  print(node.value)
  postorder(node.left)
  postorder(node.right)
  ```

- level order
  - performed using BFS

### Hash Table

_Basics not included for time sake._

- Collision resolution strategies
  - Separate Chaining
    - maintains a data structure, usually a linked list, to hold all the different values with the same hash.
  - Open addressing
    - finds another place in the hash table for the object to go by offsetting it from the position it was hashed to.
    - Key-value pairs are stored in the table itself, need to keep track of load factor.
    - Load factor (α) = items in table / size of table
      - Load factor threshold keeps lookups last, recreate larger hash table when load factor exceeded.
    - Can find new address using linear probing, quadratic probing, double hashing, pseudo random number generator (RNG seeded with key), etc.
    - Big issue if your probing sequence creates a cycle shorter than the table size (infinite looping).
      - In general, this issue is avoided by using a probing function that produces a cycle of exactly length N (size of table)
      - Linear Probing Requirement (P(x) = ax): Greatest Common Denomination (GCD) of N and a must be 1
      -

| Complexity | Avg    | Worst |
| ---------- | ------ | ----- |
| Insertion  | O(1)\* | O(n)  |
| Removal    | O(1)\* | O(n)  |
| Search     | O(1)\* | O(n)  |

\*only true if you have a good **uniform hash function**

## Algorithms

### Breadth First Search (BFS) Graph Traversal

Implemented using a queue.

```psuedocode
Let Q by a Queue
Q.enqueue(starting_node)
starting_node.visited = true

While Q is not empty Do

  node = Q.dequeue()

  For neighbor in neighbors(node):
    If neighbor has not been visited:
       neighbor.visited = true
       Q.enqueue(neighbor)
```

### Depth First Search (DFS) Graph Traversal

Implemented using a stack.

```psuedocode
DFS(G,v)   ( v is the vertex where the search starts )
      Stack S := {};   ( start with an empty stack )
      for each vertex u, set visited[u] := false;
      push S, v;
      while (S is not empty) do
        u := pop S;
        if (not visited[u]) then
            visited[u] := true;
            for each unvisited neighbour w of u
              push S, w;
        end if
      end while
  END DFS()
```

### Kruskal's Minimum Spanning Tree

- Given a graph, G = (V, E), we want to find a **Minimum Spanning Tree** in the graph (it may not be unique).
- A MST is a subset of the edges that connect all vertices in the graph with the minimal total edge cost.

Steps:

1. Sort edges by ascending edge weight
2. Walk through the sorted edges and look at the two vertices that the edge belongs to.
   - If the vertices are already unified, we do not include this edge
   - If the vertices are not already unified, we include this edge and unify the vertices
3. The algorithm terminates when every edge has been processed or all the vertices have been unified.
