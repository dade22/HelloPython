
myList = [1, 2, 3, 4, 5, 6]
print(myList) #=> [1, 2, 3, 4, 5, 6]

mySlice = myList[2:5]
print(mySlice) #=> [3, 4, 5]

mySlice = myList[5:]
print(mySlice) #=> [6]

mySlice = myList[:5]
print(mySlice) #=> [1, 2, 3, 4, 5]

mySlice = myList[:]
print(mySlice) #=> [1, 2, 3, 4, 5, 6]

myList[0:2] = [0, 1]
print(myList) #=> [0, 1, 3, 4, 5, 6]

#has the same effect as

myList = [1, 2, 3, 4, 5, 6]
myList[0]=0
myList[1]=1
print(myList) #=> [0, 1, 3, 4, 5, 6]

m=0
for e in myList:
    if m<e:
        m=e
print(m) #=>6

m=0
for i in range(len(myList)):
    if m<myList[i]:
        m=myList[i]
print(m) #=>6
