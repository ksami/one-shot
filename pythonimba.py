# we denote comment in python by #
import math					 # include math.h
radius= float(input("Enter the radius: ")) 	 #input always string
circumference = 2 * math.pi * radius		 #every var in python is treated as object
area = math.pi * radius**2			 # ** = power
print()						 # line break/ empty line
print("The circumference of circle is: ", circumference,\  # \ to continue next line
	", and the area is: ", area)

print "*" 20
print()
print "\tLegend of Zelda"
print()
print 'Is\'nt interesting?'
import keyword
print keyword.kwlist

numbers = [22,34,12,32,4]
size = len(numbers)
print size

import random
while (True):					 #All control flow statements must end with :
	val = random.randint(1,30)
	print val
	if (val is 10):
		break
for i in range(100):
	print i

for i in range(5):
	for j in range(5):
		print i + j

list = [1,2,3,4,5,6,7,8,9,10]
print list[1:9:2]				 #start end increment
print list[::-1]				 #default 1st last 1
print list[2::4]
print list

