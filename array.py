import array as arr

arrName= arr.array('i', [12,6,8,9,5])

#operations on array

#1. adding data
#append()
arrName.append(18)
print("After append:", arrName) #the appended valued will add at the last of array

#insert()
arrName.insert(2,15) #2 is index position where 15 will be inserted
print("after insert:", arrName)


