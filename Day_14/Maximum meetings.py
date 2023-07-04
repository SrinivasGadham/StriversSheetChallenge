from os import *
from sys import *
from collections import *
from math import *

def maximumMeetings(start, end):

    main_list=[]

    for i,j,k in zip(start,end,range(1,len(start)+1)):

        main_list.append([i,j,k])

    main_list.sort(key=lambda x:x[1])

    #print(main_list)

    end_time=-1

    res=[]

    for i in main_list:

        if end_time<i[0]:

            res.append(i[2])

            end_time=i[1]

    return res