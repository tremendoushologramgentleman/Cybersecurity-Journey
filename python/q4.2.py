username="scarface"
password="scarface123"
attempts=3
while attempts>0:
	username=(input("Enter the username:"))
	password=(input("Enter the password:"))
	if (username=="scarface" and password=="scarface123"):
		print("Welcome scarface!, acess granted")	
		break
	else:
		attempts=attempts-1
		print(f"Wrong attempt, {attempts}remaining")
if attempts==0:
	print("Account locked!, Too many attempts")




