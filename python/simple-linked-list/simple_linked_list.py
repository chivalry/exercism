from __future__ import annotations


class Node:
    """Represents a node within a linked list, storing a value and a pointer to the next
    node.
    """

    def __init__(self, value):
        """Initialize the node to have the given value and a next of `None`."""
        self._value = value
        self._next = None

    def value(self) -> any:
        """Return the value stored in the node."""
        return self._value

    def next(self) -> Node:
        """Return the node pointed to by `_next`."""
        return self._next


class LinkedList:
    """Represents a linked list of nodes where each individual node points to the next node
    in the linked list."""

    def __init__(self, values: list[any] = []):
        """Initialize the linked list with the values found in the passed native list."""
        self._head = None
        for value in values:
            self.push(value)

    def __len__(self) -> int:
        """Return the number of nodes in the linked list."""
        len = 0
        node = self._head
        while node:
            len += 1
            node = node.next()
        return len

    def __iter__(self) -> LinkedList:
        """Initialize a variable to point to the head and return the self, which has a
        `__next__` method."""
        self._pointer = self._head
        return self

    def __next__(self) -> any:
        """"""
        if self._pointer == None:
            del self._pointer
            raise StopIteration
        value = self._pointer.value()
        self._pointer = self._pointer.next()
        return value

    def head(self) -> Node:
        """Return the node pointed to by the `_head`."""
        if self._head == None:
            raise EmptyListException('The list is empty.')
        return self._head

    def push(self, value) -> None:
        """Add the given value to the linked list (enclosed within a node), updating the
        `_head` to point to the new node and the node to point to the previous `_head`."""
        node = Node(value)
        node._next = self._head
        self._head = node

    def pop(self) -> any:
        """Remove the head node from the linked list, storing the second node as the current
        head and returning the value of the previous head node."""
        if len(self) == 0:
            raise EmptyListException('The list is empty.')
        popped = self._head.value()
        self._head = self._head.next()
        return popped

    def reversed(self) -> LinkedList:
        result = []
        for value in self:
            result = [value] + result
        return result


class EmptyListException(Exception):
    """Exception raised when the linked list is empty.

    message: explanation of the error.
    """

    def __init__(self, message):
        """Initialize the exception using the provided message."""
        self.message = message
