# we denote comment in python by #
import math					 # include math.h

integer = 8 / 3 			 #in python 3.x, this will yield float. no int division.
print integer				 #but this is python 2.7. so..

radius= float(input("Enter the radius: ")) 	 #input always string
circumference = 2 * math.pi * radius		 #every var in python is treated as object
circumference = int(circumference+0.5)		 #round off to nearest integer
area = math.pi * radius**2			 # ** = power
print()						 # line break/ empty line
print("The circumference of circle is: ", circumference,\
	", and the area is: ", area)             # \ to continue next line

print "*" * 20
print()
print "\tLegend of Zelda"
print()
print 'Is\'nt interesting?'
import keyword
print keyword.kwlist

numbers = [22,34,12,32,4]
size = len(numbers)
print size

tsicba = "They said i could be anything"
print tsicba
tsicba = "So i chose boolean"
print tsicba
tsicba = False
print tsicba
tsicba = 3 + 1j
type(tsicba)

import random
while (True):					 #All control flow statements must end with :
	val = random.randint(1,30)
	print val
	if (val is 10):
		break
for i in range(25):
	print i

for i in range(5):
	for j in range(5):
		print i + j

list = [1,2,3,4,5,6,7,8,9,10]                    #start end increment
print list[1:9:2]				 #default 1st last 1
print list[::-1]				 #start from the back
print list[2::4]
print list

max(3,4,5,6,78,9,10)
min(numbers)