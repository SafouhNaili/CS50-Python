# crearte an empty set

s=set()

#add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
#no element apears twice in a set
s.add(3)
#remove
s.remove(2)
print(s)
#len = length
print(f"the set has {len(s)} elements.")