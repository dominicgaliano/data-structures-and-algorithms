# Using python native linked list to eliminate
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque

    def __str__(self):
        output = ""

        for element in q:
            output += f"{element} "

        return output.strip()

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

    def peek(self):
        pass
