def horses_like_hay(hay_count, barns):
    print "You have %d bails of hay!" % hay_count
    print "You have %d barns for your horses!" % barns
    print "That is a great load ya got there \n"


print "defining horses_like_hay using direct numbers"
horses_like_hay(20,3)


print "defining horses_like_hay as variables"
hay_count = 20
barns = 3


horses_like_hay(hay_count, barns)


print "defining horses_like_hay with variables and math"
horses_like_hay(10+2-3 + hay_count, 29+9-10-barns)



