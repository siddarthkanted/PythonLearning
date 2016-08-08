import sys



#list comprehensions. generate a list of numbers without for loop.
x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
z = int(sys.stdin.readline())
n = int(sys.stdin.readline())
list = [[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c != n]
print(list)
				


#tuples. A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
n = int(sys.stdin.readline())
line = sys.stdin.readline()
array = line.split(" ")
tupleObject = tuple(map(lambda x:int(x), array))
print(hash(tupleObject))



#list data type
list = []


a = int(sys.stdin.readline())
for i in range(0,a):
	line = sys.stdin.readline()
	if(line.__contains__("insert")):
		array = line.split(" ")
		if int(array[1]) == 0:
			list= [int(array[2])]+list
		elif int(array[1]) == len(list):
			list.append(int(array[2]))
		else:
			list=list[:int(array[1])] + [int(array[2])] + list[int(array[1]):len(list)]


	if(line.__contains__("print")):
		print(list)
	
	if(line.__contains__("remove")):
		array = line.split(" ")
		list.remove(int(array[1]))
	
	if(line.__contains__("append")):
		array = line.split(" ")
		list.append(int(array[1]))

	if(line.__contains__("sort")):
		list.sort()
	
	if(line.__contains__("pop")):
		list.pop()
	
	if(line.__contains__("reverse")):
		list.reverse()

