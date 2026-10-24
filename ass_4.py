#assignment pre_4
lan = ['Gujarati','Hindi','English','Marathi']

print("Original list",lan)
lan.insert(0,'Sanskrit')
print("After insertion",lan)

lan.remove(lan[4])
print("After removal",lan)

lan.append(lan[0])
#lan.append('nepali')
print("After appending",lan)

len(lan)
print("length of list",len(lan))

lan.pop()
print("After pop",lan)

del lan[0]
print("After deleting",lan)

lan.clear()
print("After clearing",lan)