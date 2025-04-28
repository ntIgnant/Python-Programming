# The first class 'struct' is for the actual Node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None # Pointer that points to the next node (initially pointing to nothing)


# The second class 'struct' is for the actual Linkedlist
class LinkedList:
    def __init__(self):
        self.head = None # The initial head of the list is 'nothing' NULL/None

    def append(self, data):
        # Add a nde node with the given data
        new_node = Node(val=data) # assign the value

        # If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return

        # If the list is not empty, traverse to the end of the list and append the new node
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node # append the new node at the end of the list
        print("The data was successfully appended!")


if __name__ == "__main__":

    my_list = LinkedList() # creates a SinglyLinkedList object
    new_node_data = str(input("Please enter something to add to the LinkedList: "))
    my_list.append(new_node_data) # append the new input data

