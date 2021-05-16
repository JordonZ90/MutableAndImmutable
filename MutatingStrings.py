name = 'Bitty a cat'
new_name = f"{name[0:6]}the{name[7:11]}"
print(name)
print(new_name)

box = [1, 2, 3]
box = [4, 5, 6]
#print(box)

# The list box isn't being altered but overwritten
# To change the actual list this is required

box = [1, 2, 3]
del box[2]
del box[1]
del box[0]
box.append(4)
box.append(5)
box.append(6)
print(box)