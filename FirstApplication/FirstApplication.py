#map function
import sys
map(lambda x : sys.stdout.write(str(x)),range(1,int(sys.stdin.readline()) +1))

#leap year
def isLeapYear( n ):
	if n%100==0 and n%400==0:
		return True
	if n%100!=0 and n%4==0:
		return True
	return False

import sys
a = int(sys.stdin.readline())
print(isLeapYear(a))


#for loop
import sys
a = int(sys.stdin.readline())
for i in range(0,a):
	print(i**2) #Exponent



#print statement in python
a="hello python"
print(a)

#read from console in python
import sys
a= sys.stdin.readline()
print(a)

#operators
import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
print(a+b)
print(a-b)
print(a*b)
print(a//b) #integer division
print(float(a)/float(b))	# float division

#if statement python
import sys
a = int(sys.stdin.readline())
if(a%2!=0):
	print("Weird")
if(a%2==0 and a>=2 and a<=5):
	print("Not Weird")
if(a%2==0 and a>=6 and a<=20):
	print("Weird")
if(a%2==0 and a>20):
	print("Not Weird")



