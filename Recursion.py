
'''
Implementing a singly linked list using recursive functions.
'''
 
class LinkedNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = '_value', '_next'

    def __init__(self, value, next=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next: pointer to the next node in the LinkedList, default is None
        """
        self._value = value  # element at the node
        self._next = next  # reference to next node in the LinkedList

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self._value)

    __str__ = __repr__

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_value(self, value):
        self._value = value

    def set_next(self, next):
        self._next = next


# IMPLEMENT THESE FUNCTIONS - DO NOT MODIFY FUNCTION SIGNATURES #

def insert(value, node=None):
    """
    Insert given value into the linked list that has head node
    :param value: the value to be inserted
    :param node: the head node of the linked list
    :return: starting node of the linked list
    """
    if node is None:
        new = LinkedNode(value)
        # node._value = new
        return new
    elif node._next is None:
        new = LinkedNode(value)
        node._next = new
        return node
    elif node._next is not None:
        insert(value, node._next)
        return node

def to_string(node):
    """
    Generates a string representation of the list
    :param node: head node of the given linked list
    :return: the string representation of the list
    """
    if node is None:
        return ""
    if node._next is None:
        return str(node)
    elif node._next is not None:
        return str(node) + ", " + to_string(node._next)

def remove(value, node):
    """
    Removes the first node in the list with the given value
    :param value: the value to be removed
    :param node: the head node of the linked list
    :return: the starting node of the linked list
    """
    if node is None:
        return node
    if node._value == value:
        new = node._next
        return new
    node._next = remove(value, node._next)
    return node


def remove_all(value, node):
    """
    Removes all nodes in the list with the given value
    :param value: the value to remove
    :param node: the head node in the linked list
    :return: the starting node of the linked list
    """
    if node is None:
        return node
    node._next = remove_all(value, node._next)
    if value == node._value:
        node = node._next
    return node

def search(value, node):
    """
    Looks for value in linked list
    :param value: the value to be searched for
    :param node: the head node of the linked list
    :return: True if the value is found, false if otherwise
    """
    final = False
    if node is None:
        return final
    if node._next is None:
        if node._value == value:
            final = True
        else:
            final = False
    elif node._next is not None:
        if node._value == value:
            final = True
        else:
            return search(value, node._next)
    return final

def length(node):
    """
    Calculates length of the list
    :param node: head node of the linked list
    :return: an integer representing the length
    """
    if node is None:
        return 0
    return length(node._next) + 1

def sum_list(node):
    """
    Calculates the sum of the list
    :param node: head node of the linked list
    :return: an integer representing the sum of the list
    """
    if node is None:
        return 0
    return sum_list(node._next) + node._value

def count(value, node):
    """
    Counts all said value in given list
    :param value: the value to be counted
    :param node: the list to be searched
    :return:
    """
    if node is None:
        return 0
    if node._value == value:
        return count(value, node._next) + 1
    else:
        return count(value, node._next)

def reverse(node):
    """
    Reverse list
    :param node: head node of the list to be reverse
    :return: the head node of the reversed list
    """
    if node is None:
        return node
    if node._next is None:
        return node
    new = reverse(node._next)
    node._next._next = node
    node._next = None
    return new

def list_percentage(node, percentage, counter=0):
    """
    Returns a subset of the percent of the original list passed in.
    :param node: starts with the head node of the list passed in
    :param percentage: the percentage of the entire list to be returned
    :param counter: keeping track of the length of the list
    :return: the first node in the subset of the list subset
    """
    if percentage == 1.0:
        return node
    elif percentage == 0:
        return None
    else:
        if node._next is None:
            return counter
        else:
            percent = 1 - percentage
            cnt = list_percentage(node._next, percentage, counter + 1)
            if percent >= .5:
                if isinstance(cnt, int) and (cnt * percent) >= counter:
                    return node._next
                else:
                    return cnt
            elif percent < 0.5:
                if isinstance(cnt, int) and (cnt * percent) >= counter:
                    return node._next
                else:
                    return cnt

