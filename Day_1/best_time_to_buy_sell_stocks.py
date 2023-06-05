from os import *
from sys import *
from collections import *
from math import *


def maximumProfit(prices):
    n = len(prices)
    suffix_sum = [-1 for i in range(len(prices))]
    suffix_sum[-1] = prices[-1]
    for i in range(n-2, -1, -1):
        suffix_sum[i] = max(prices[i], suffix_sum[i+1])
    max_price = float('-inf')
    for i in range(len(prices)):
        max_price = max(suffix_sum[i]-prices[i], max_price)
    return max_price

    # Write your code here.
