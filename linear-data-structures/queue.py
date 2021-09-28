from nodes import Node

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None

  def peek(self):
    return self.head.get_value()