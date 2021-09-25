class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    # Insert new head node
    def insert_beginning(self, new_value):
        new_node = Node(new_value) # instantiate a Node with new_value. Name this new_node
        new_node.set_next_node(self.head_node) # link new_node to the existing head_node
        self.head_node = new_node # replace the current head_node with new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()
        return string_list

    # Returns data at given index in linked list
    def get_nth(self, index):
        current = self.get_head_node()  # Initialise temp
        count = 0  # Index of current node

        # Loop while end of linked list is not reached
        while current:
            if count == index:
                return current.get_value()
            count += 1
            current = current.get_next_node()

        # if we get to this line, the caller was asking
        # for a non-existent element so we assert fail
        assert false
        return 0

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        # Before traversing, check if it's the head_node being removed.
        # If it is, set the second node as the head node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def remove_nodes(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()

        while current_node:
            next_node = current_node.get_next_node()
            if next_node is not None:
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    continue
                else:
                    current_node = next_node
            else:
                current_node = None

ll = LinkedList(5)
ll.insert_beginning("Hey")
ll.insert_beginning(5675)
ll.insert_beginning("Hey")
ll.insert_beginning(90)
ll.remove_nodes("Hey")
print(ll.stringify_list())