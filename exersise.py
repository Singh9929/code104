name,age=input("Enter name and age with , seperated").split(",")
age=int(age)
name=name.lower()
if name[0]=="a" and age>=10:
	print("You can watch")
else:
	print("You can not watch.")	
	
