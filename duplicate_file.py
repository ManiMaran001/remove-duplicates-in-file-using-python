# read a entire file and remove the duplicates and spaces task fun
def pass_to_newfile(new):
	count=0
	with open('james.txt','w') as fil:
		for i in new:
			print(i,file=fil)
			count+=1
	print("overall count new  file",count)
	
	
def remove_duplicates(name):
	count=0
	sets=set()
	with open(name,'r') as fil:
		for i in fil:
			sets.add(i.strip(" "))
			count+=1
	print("overall count old file",count)
	new_sets=set()
	for i in sets:
		new_sets.add(i.strip('\n'))
	print(new_sets)
	pass_to_newfile(new_sets)
	
	
name="dup.txt"
remove_duplicates(name)
