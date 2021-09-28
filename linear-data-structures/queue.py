from nodes import Node


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        # Check if there's space in the queue
        if self.has_space():
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            # Check if the queue is empty
            # If it is, the new item becomes the head and the tail
            # If it isn't, it just becomes the new tail
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")

    def dequeue(self):
        # Check if the queue isn't empty
        if not self.is_empty():
            item_to_remove = self.head
            print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
            # Check if there's only one item in the queue
            # If there is, set the head and tail to None
            # If there isn't, set the head to the second item in the queue
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("This queue is totally empty!")

    def peek(self):
        if self.is_empty():
            print("Nothing to see here!")
        return self.head.get_value()

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size is not None:
            return self.max_size > self.get_size()
        return True

    def is_empty(self):
        return self.get_size() == 0