import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0

        # DLL to store our elements
        self.storage = DoublyLinkedList()


    def enqueue(self, value):
        # add itme to the back of the queue
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        # remove and return an item from the front of queue
        if self.size == 0:
            return
        else:
            value = self.storage.remove_from_tail()
            self.size -= 1
            return value

    def __len__(self):
        # returns the number of items in our queue
        return self.size
