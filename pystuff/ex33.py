# a while loop will keep executing the code block under it as long as a boolean expression is TRUE. That means they can go on forever sometimes. For-loops are better often. 

i = 0
numbers = []

while i < 6:
    print "at the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num 


