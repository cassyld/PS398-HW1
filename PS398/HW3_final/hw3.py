import time
import math
import csv
import random

n = 1000
list1 = []

selSort_times = [ ]
bubble_times = [ ]


def random_list(n):
   list1 = list()
   for i in range (0, n):
       list1.append(random.randint(0, n-1))
   return list1

#def randomList(n):
 #   def __init__(self, n):
  #  self.list = []
   # for i in range(0,n):
    #    self.list.append(random.randint(0,n-1))

#First up: Selection_sort. The internet tells me that it is simple. 
# it is basically putting a deck of cards back in order. Just keep
# looking for the smallest value and order based on this. The logic
# is like that of a loop. Each time we go through it we select the smallest
# of the remaining elements and move it into its proper position.

def selection_sort(list1):

    start = time.clock()
    for i in range(0, len (list1)):
        min = i
        for j in range (i + 1, len(list1)):
            if list1[j] < list1[min]:
               min =j
        list1[i], list1[min] = list1[min], list1[i]
           
    end = time.clock()
    selSort_times.append(end-start)


def bubble_sort(list1):
    start = time.clock()
    #swap_test = False
    for i in range(0, len(list1) - 1):
        swap_test = False
        for j in range(0, len(list1) - i - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]  # swap
            swap_test = True
        if swap_test == False:
            break
    end = time.clock()
    bubble_times.append(end-start)

#Write these times to a csv names times.csv where each time gets its own column

csvWriter = csv.writer(open('times.csv', 'wb'))

for i in range(0,len(selSort_times)):

  csvWriter.writerow([selSort_times[i], bubble_times[i]])


 
