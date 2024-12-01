from __future__ import annotations


class EmptyListException(Exception):
    pass


class Node:
    """Represents a node of a linked list, storing a value and a pointer to the next node."""

    def __init__(self, value: any, next: Node = None):
        """Initialize the node to have the given value and a next of `None`."""
        self._value = value
        self._next = next

    def value(self) -> any:
        """Return the value stored in the node."""
        return self._value

    def next(self) -> Node:
        """Return the node pointed to by `_next`."""
        return self._next


class LinkedList:
    """Represents a linked list of nodes where each node points to the next one in the list."""

    def __init__(self, values: list[any] = None):
        """Initialize the linked list with the values found in the passed native list.
        :param values: list[any] - A list of values to add to the linked list"""
        if values == None:
            values = []
        self._head = None
        for value in values:
            self.push(value)

    def __len__(self) -> int:
        """Return the number of nodes in the linked list.
        :return int - The number of nodes in the linked list
        """
        length = 0
        node = self._head
        while node:
            length += 1
            node = node.next()
        return length

    def __iter__(self) -> LinkedList:
        """Initialize a variable to point to the head and return the iterable self.
        :return LinkedList - Return the `self`, which has a `__next__` method
        """
        self._pointer = self._head
        return self

    def __next__(self) -> any:
        """Return the next node pointed to by `_pointer`, deleting it if the iterable is done.
        :return any: The value of the node currently pointed to by `_pointer`
        """
        if self._pointer == None:
            del self._pointer
            raise StopIteration
        value = self._pointer.value()
        self._pointer = self._pointer.next()
        return value

    def head(self) -> Node:
        """Return the node pointed to by the `_head`.
        :return Node - Return the node pointed to by the `_head`
        """
        if self._head == None:
            raise EmptyListException('The list is empty.')
        return self._head

    def push(self, value):
        """Add the given value to the start of the linked list.
        :param value: any - The value to push onto the linked list
        """
        node = Node(value, self._head)
        self._head = node

    def pop(self) -> any:
        """Remove the head node from the linked list, returning its value.
        :return any - The value of the node pointed to by `_head`
        """
        if len(self) == 0:
            raise EmptyListException('The list is empty.')
        popped = self._head.value()
        self._head = self._head.next()
        return popped

    def reversed(self) -> list[any]:
        """Return a list representing the reversed values of the nodes in the list.
        :return list[any] - A list of values in reversed order from that in the linked list
        """
        linked = LinkedList()
        for value in self:
            linked.push(value)
        return linked
