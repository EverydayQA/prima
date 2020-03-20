

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = Node(data='HEAD')

    def append(self, data):
        # creating the node with the data parameter
        new_node = Node(data=data)
        if self.head is None:
            self.head.next = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        # when we have reached the end of list
        current_node.next = new_node

    def display(self):
        # container for the nodes
        node_elements = []
        current_node = self.head
        node_elements.append(current_node.data)
        while current_node.next is not None:
            current_node = current_node.next
            node_elements.append(current_node.data)
        print(node_elements)

    def insert_as_first_element(self, data):
        # head is not to be changed except head.next
        new_node = Node(data=data)
        new_next = self.head.next;
        self.head.next = new_node
        new_node.next = new_next


if __name__ == '__main__':
    ll = Linkedlist()
    ll.display()
    ll.append('a')
    ll.display()
    ll.insert_as_first_element('b')
    ll.display()
