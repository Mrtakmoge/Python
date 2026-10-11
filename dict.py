#dictionary: key=>val

marks={"Math":99,"Phy":93,"Chem":98}
print("Dict:",marks)
print("Marks of physics:",marks["Phy"])
#Adding value to dict
marks["Eng"]=95


for key in marks:
    print(key,marks[key])
    