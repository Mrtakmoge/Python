#List is Mutable
print("List:")
marks=[1,2,3,4]
print(marks)


#Operations on list:
print("Lenght of list:")
print(len(marks))

#index:
print("Index:1:")
print(marks[1])

#slicing: listname[1st indexno.:endindex]
print("Slicing:")
print(marks[1:4])

#add value to list:
marks.append(5)
marks.insert(0,0)#listname.insert(indexno,value)

print("Loopn on list: ")
for i in marks:
    print(i)
