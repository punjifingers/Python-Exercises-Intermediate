# print funstion practices

#print function parameters

## random
# print("a\n",1, sep='')
# print("b\n",2)
# print("c\n",3, end='')
# print("d\n",4)
# print("e\n",5)

#sep
print("a",1, sep='')
print("b",2)
print("c",3, sep='\n')
print("d",4)

#end
print("a",1, end='')
print("b",2)
print("c",3, end='\n')
print("d",4)

#file
f = open("p1.txt", "w")#p1.txt file will be created in the same directory(the work directory) where the script is running
print("a",1, file=f)
print("b",2, file=f)
f.close()


#flush
print("a",1, flush=True)
print("b",2)

