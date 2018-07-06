d=dict()
for i in range(0,2):
	num=int(input("enter num:"))
	name=raw_input("enter name:")
	d[num]=name
print d	

x=int(input("enter choice: 1.get name,2.get number,3.display dictionary,4.insert:::"))
if x == 1:
	print d[int(input("enter num:"))]
elif x == 2:
	n=d.keys()	
	print n
elif x==3:
	print d



	
