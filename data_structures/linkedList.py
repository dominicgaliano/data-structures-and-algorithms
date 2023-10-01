"""
Linked List - Sequential list of nodes that holds data which point to
              other nodes also containing data.

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
"""


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        stringOutput = ""

        # traverse list and print all values
        currNode = self.head
        i = 0
        while currNode:
            stringOutput += f"{currNode.value} "
            currNode = currNode.nextNode
            i += 1

        return stringOutput.strip()

    def append(self, value):
        """Append new node with value 'value' at end of list"""
        newNode = Node(value)

        # set old tail node to point to new node
        if self.tail:
            self.tail.nextNode = newNode

        # set list tail pointer to point to new node
        self.tail = newNode

        # special case, first addition to list
        if not self.head:
            self.head = newNode

    def insertAt(self, positionValue, newValue):
        """Insert node with newValue before first node with value
        positionValue. Returns newly created Node if successful"""

        # if no nodes in list, return False
        if not self.head:
            return None

        # traverse list until one node before node with positionValue
        currNode = self.head
        while currNode.nextNode and currNode.nextNode.value != positionValue:
            currNode = currNode.nextNode

        # if end of list reached, return None
        if not currNode:
            return None

        newNode = Node(newValue)

        # edge case, inserting at end of list
        if not currNode.nextNode:
            self.tail = newNode

        # redirect two pointers to newNode
        newNode.nextNode = currNode.nextNode
        currNode.nextNode = newNode

        return newNode

    def delete(self, positionValue):
        """
        Delete first node with positionValue, returns deleted node if
        successful and None if unsuccessful.
        """
        # edge case, empty list
        if not self.head:
            return None

        # init two pointers to traverse
        trav1 = self.head
        trav2 = self.head.nextNode

        # shift both nodes along until trav2.value = positionValue
        while trav2 and trav2.value != positionValue:
            trav1 = trav1.nextNode
            trav2 = trav2.nextNode

        # no positionValue found
        if not trav2:
            return None

        # edge case, removed last node
        if not trav2.nextNode:
            self.tail = trav1

        # redirect trav1 pointer
        removedNode = trav2
        trav1.nextNode = trav2.nextNode

        return removedNode


def main():
    # singly linked list demo
    # generate dummy data and insert
    list1 = SinglyLinkedList()
    for i in range(10):
        list1.append(i)

    print(list1)

    # successful and unsuccessful insertAt
    list1.insertAt(5, 10)
    list1.insertAt(11, 10)

    print(list1)

    # successful and unsuccessful delete
    list1.delete(10)
    list1.delete(11)

    print(list1)


if __name__ == "__main__":
    main()
