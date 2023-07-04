from os import *
from sys import *
from collections import *
from math import *

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):

    denominations = [1,2,5,10,20,50,100,500,1000]

    coins = 0

    denominations = denominations[::-1]

    for i in denominations:

        if isinstance(amount%i,int) :

            n = amount//i

            coins += n

            amount -= i*n

    return coins

    