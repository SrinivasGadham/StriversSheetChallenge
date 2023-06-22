from os import *
from sys import *
from collections import *
from math import *

class Queue :

    #Define data members and __init__()




    '''----------------- Public Functions of Queue -----------------'''
    def __init__(self):
 
        self.queue = []
        # self.front = self.rear = 0
        # self.capacity = c

   
    def isEmpty(self) :
        if len(self.queue)==0:
            return 1
        return 0
        #Implement the isEmpty() function



    def enqueue(self, data) :
        self.queue.append(data)
        #Implement the enqueue(element) function



    def dequeue(self) :
        if len(self.queue) < 1:
            return -1
        return self.queue.pop(0)


    def front(self) :
        #Implement the front() function
        if len(self.queue) < 1:
            return -1
        return self.queue[0]
