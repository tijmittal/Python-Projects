print("-"*50)
print("Welcome to PYT Registration!")
print("-"*50)

account = "1"

x = str(input("To create a new account Press 1 ----> "))
if x == "1":
	print("-"*50)
	x1 = str(input("Enter your name:"))
	x2 = str(input("Enter your mobile number:"))
	x3 = str(input("Enter your D.O.B.(DD/MM/YYYY):"))
	x4 = str(input("Enter your email ID:"))
	x5 = str(input("Enter new User ID:"))
	x6 = str(input("Enter Password:"))
	x7 = str(input("Confirm your Password:"))
	if x7==x6:
		print("-"*50)
		print("Thank you!\nYour account has been created!")
		print("-"*50)
		x8 = str(input("Press 2 to login to your account.\nPress 'E' to exit.\nSelect an option:"))
		if x8=="2":
			x9 = str(input("Enter your User ID:"))
			if x9==x5:
				x10 = str(input("Enter your Password:"))
				if x10==x7:
					print("-"*50)
					print("Here are your account details:")
					print("-"*50)
					print("User Name:",x1)
					print("User Mobile Number:",x2)
					print("User D.O.B.:",x3)
					print("User Email ID:",x4)
					print("User ID:",x5)
					print("-"*50)
				elif x10!=x7:
					print("-"*50)
					print("Password do not match!")
					x11 = str(input("Please Re-enter your password:"))
					if x11==x6:
						print("-"*50)
						print("Here are your account details:")
						print("-"*50)
						print("User Name:",x1)
						print("User Mobile Number:",x2)
						print("User D.O.B.:",x3)
						print("User Email ID:",x4)
						print("User ID:",x5)
						print("-"*50)
					else:
						print("-"*50)
						print("Wrong Password entered!\nPlease try again later!")
						print("-"*50)
				else:
					print("-"*50)
					print("Wrong Password entered!\nPlease try again later!")
					print("-"*50) 
			else:
				print("-"*50)
				print("You probably entered wrong User ID!\nTry again!")
				print("-"*50)
		elif x8=="E":
			print("-"*50)
			print("Thank You!")
			print("-"*50)

		else:
			print("-"*50)
			print("Invalid Input!")
			print("-"*50)
	elif x7!=x6:
		print("-"*50)
		print("Password do not match!")
		print("-"*50)
		x12 = str(input("Please Re-enter your password:"))
		if x12==x6:
			print("-"*50)
			print("Thank you!\nYour account has been created!")
			print("-"*50)
			x13 = str(input("Press 2 to login to your account.\nPress 'E' to exit.\nSelect an option:"))
			if x13=="2":
				x14 = str(input("Enter your User ID:"))
				if x14==x5:
					x15 = str(input("Enter your Password:"))
					if x15==x6:
						print("-"*50)
						print("Here are your account details:")
						print("-"*50)
						print("User Name:",x1)
						print("User Mobile Number:",x2)
						print("User D.O.B.:",x3)
						print("User Email ID:",x4)
						print("User ID:",x5)
						print("-"*50)
					elif x15!=x6:
						print("-"*50)
						print("Password do not match!")
						x16 = str(input("Please Re-enter your password:"))
						if x16==x6:
							print("-"*50)
							print("Here are your account details:")
							print("-"*50)
							print("User Name:",x1)
							print("User Mobile Number:",x2)
							print("User D.O.B.:",x3)
							print("User Email ID:",x4)
							print("User ID:",x5)
							print("-"*50)
						else:
							print("-"*50)
							print("Wrong Password entered!\nPlease try again later!")
							print("-"*50)
					else:
						print("-"*50)
						print("Wrong Password entered!\nPlease try again later!")
						print("-"*50) 
				else:
					print("-"*50)
					print("You probably entered wrong User ID!\nTry again!")
					print("-"*50)
			elif x13=="E":
				print("-"*50)
				print("Thank You!")
				print("-"*50)

			else:
				print("-"*50)
				print("Invalid Input!")
				print("-"*50)
		elif x12!=x6:
			print("-"*50)
			print("Wrong password entered!\nPlease try again later!")
			print("-"*50)
	else:
		print("-"*50)
		print("Again Wrong Password entered!\nTry again after sometime.")
		print("-"*50)
else:
	print("-"*50)
	print("Invalid Input!\nTry again!")
	print("-"*50)
		


