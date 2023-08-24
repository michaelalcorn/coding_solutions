"""
QUEUE USING STACK

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

"""

class MyQueue(object):

    def __init__(self):
        # self.which_stack = True
        # self.true_stack = []
        # self.false_stack = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.insert(0,x)

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop(len(self.stack)-1)

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0 
    