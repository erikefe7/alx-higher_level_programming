#!/usr/bin/python3
""" A class that defines the node of a singly linked list """


class Node:
    """ the node of the sigly linked list
    """

    def __init__(self, data, next_node=None):
        """ initializing the node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ retrieving the property of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ setting the value of the node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ retrieving the private node data
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ using the retrieved private data to complete the list
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __str__(self):
        """ the singly linked list
        """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """ the initialization of the value of the head node
        """
        self.__head = None

    def sorted_insert(self, value):
        """ adding value to the node
        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
