for key,value in values.items():
	print (key,value)

dictionary = {'george' : 16, 'amber' : 19}
search_age = raw_input("Provide age")
for age in dictionary.values():
    if age == search_age:
        name = dictionary[age]
        print name


if x == 'a':
    # Do the thing
elif x == 'b':
    # Do the other thing
if x in 'bc':
    # Fall-through by not using elif, but now the default case includes case 'a'!
elif x in 'xyz':
    # Do yet another thing
else:
    # Do the default
