#--------------------------Creted by Kshitij Mittal-----------------------------
#-------------------Thanks for visiting my github profile-----------------------

#-------------------------------enjoy coding!-----------------------------------

print("-"*50)
print("Welcome!\nLet's create a virtual GST bill!")
print("-"*50)
print("Welcome to koffeegasm!")
print("-"*50)

system_security_code = 1234

bill = "a"
check_price = "b"

cold_coffee   = "001"	#Rs.129
croissant     = "002"	#Rs.189
cappucino     = "003"	#Rs.139
mocha         = "004"	#Rs.169
hot_chocolate = "005"	#Rs.179
iced_vannila  = "006"	#Rs.159
brownie       = "007"	#Rs.119
kitkat_shake  = "008"	#Rs.199
frappucino    = "009"	#Rs.139
oreo_shake    = "010"	#Rs.199

#prices
coffee = 122.86
croi   = 180.00
capp   = 132.38
moch   = 160.95
hot    = 170.48
iced   = 151.43
brow   = 133.33
kitkat = 189.52
frapp  = 132.38
oreo   = 189.52

x = str(input("(a)Generate a Bill: \n(b)Check Price of an item:"))
y = int(input("Enter System Security Code:"))
if x=="a" and y==system_security_code:
	x2 = str(input("Enter Customer's name:"))
	x3 = str(input("Enter Customer's mobile number:"))
	x4 = str(input("Select items:\n(001)Cold Coffee\n(002)Croissant\n(003)Cappucino\n(004)Mocha\n(005)Hot Chocolate\n(006)Iced Vannila\n(007)Brownie\n(008)Kitkat Shake\n(009)Frappucino\n(010)Oreo Shake:"))
	if x4=="001":
		print("You selected code 001: Cold Coffee")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Customer Name:",x2)
		print("Customer Mobile Phone no:",x3)
		print("-"*50)
		print("Items:\nCold Coffee  - Rs.",coffee)
		print("-"*50)
		print("CGST:",0.025*coffee ,"(2.5%)")
		print("SGST:",0.025*coffee ,"(2.5%)")
		print('-'*50)
		print("Total Amount:Rs.",round(coffee+0.05*coffee))
		print("(Including GST)")

	elif x4=="002":
		print("You selected code 002: Coissant")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Customer Name:",x2)
		print("Customer Mobile Phone no:",x3)
		print("-"*50)
		print("Items:\nCroissant  - Rs.",croi)
		print("-"*50)
		print("CGST:",0.025*croi ,"(2.5%)")
		print("SGST:",0.025*croi ,"(2.5%)")
		print('-'*50)
		print("Total Amount:Rs.",round(croi+0.05*croi))
		print("(Including GST)")

	elif x4=="003":
		print("You selected code 003: Cappucino")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Customer Name:",x2)
		print("Customer Mobile Phone no:",x3)
		print("-"*50)
		print("Items:\nCappucino  - Rs.",capp)
		print("-"*50)
		print("CGST:",0.025*capp ,"(2.5%)")
		print("SGST:",0.025*capp ,"(2.5%)")
		print('-'*50)
		print("Total Amount:Rs.",round(capp+0.05*capp))
		print("(Including GST)")

	elif x4=="004":
		print("You selected code 004: Mocha")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Customer Name:",x2)
		print("Customer Mobile Phone no:",x3)
		print("-"*50)
		print("Items:\nMocha  - Rs.",moch)
		print("-"*50)
		print("CGST:",0.025*moch ,"(2.5%)")
		print("SGST:",0.025*moch ,"(2.5%)")
		print('-'*50)
		print("Total Amount:Rs.",round(moch+0.05*moch))
		print("(Including GST)")

	elif x4=="005":
		print("You selected code 005: Hot Chocolate")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Customer Name:",x2)
		print("Customer Mobile Phone no:",x3)
		print("-"*50)
		print("Items:\nHot Chocolate  - Rs.",hot)
		print("-"*50)
		print("CGST:",0.025*hot ,"(2.5%)")
		print("SGST:",0.025*hot ,"(2.5%)")
		print('-'*50)
		print("Total Amount:Rs.",round(hot+0.05*hot))
		print("(Including GST)")

	elif x4=="006":
		print("You selected code 006: Iced Vanilla")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Customer Name:",x2)
		print("Customer Mobile Phone no:",x3)
		print("-"*50)
		print("Items:\nIced Vanilla  - Rs.",iced)
		print("-"*50)
		print("CGST:",0.025*iced ,"(2.5%)")
		print("SGST:",0.025*iced ,"(2.5%)")
		print('-'*50)
		print("Total Amount:Rs.",round(iced+0.05*iced))
		print("(Including GST)")

	elif x4=="007":
		print("You selected code 007: Brownie")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Customer Name:",x2)
		print("Customer Mobile Phone no:",x3)
		print("-"*50)
		print("Items:\nBrownie  - Rs.",brow)
		print("-"*50)
		print("CGST:",0.025*brow ,"(2.5%)")
		print("SGST:",0.025*brow ,"(2.5%)")
		print('-'*50)
		print("Total Amount:Rs.",round(brow+0.05*brow)) 
		print("(Including GST)")

	elif x4=="008":
		print("You selected code 008: Kitkat Shake")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Customer Name:",x2)
		print("Customer Mobile Phone no:",x3)
		print("-"*50)
		print("Items:\nKitkat Shake  - Rs.",kitkat)
		print("-"*50)
		print("CGST:",0.025*kitkat ,"(2.5%)")
		print("SGST:",0.025*kitkat ,"(2.5%)")
		print('-'*50)
		print("Total Amount:Rs.",round(kitkat+0.05*kitkat))
		print("(Including GST)")

	elif x4=="009":
		print("You selected code 009: Frappucino")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Customer Name:",x2)
		print("Customer Mobile Phone no:",x3)
		print("-"*50)
		print("Items:\nFrappucino  - Rs.",frapp)
		print("-"*50)
		print("CGST:",0.025*frapp ,"(2.5%)")
		print("SGST:",0.025*frapp ,"(2.5%)")
		print('-'*50)
		print("Total Amount:Rs.",round(frapp+0.05*frapp))
		print("(Including GST)")

	elif x4=="010":
		print("You selected code 010: Oreo Shake")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Customer Name:",x2)
		print("Customer Mobile Phone no:",x3)
		print("-"*50)
		print("Items:\nOreo Shake  - Rs.",oreo)
		print("-"*50)
		print("CGST:",0.025*oreo ,"(2.5%)")
		print("SGST:",0.025*oreo ,"(2.5%)")
		print('-'*50)
		print("Total Amount:Rs.",round(oreo+0.05*oreo))
		print("(Including GST)")

	else:
		print("You selected Wrong code!\nTry Again!")
	print("-"*50)
	print("Thank you!\nVisit us again!\nRegards Team Koffeegasm!")
	print("-"*50)


elif x=="b" and y==system_security_code:
	x5 = str(input("Select items:\n(001)Cold Coffee\n(002)Croissant(003)Cappucino\n(004)Mocha\n(005)Hot Chocolate\n(006)Iced Vannila\n(007)Brownie\n(008)Kitkat Shake\n(009)Frappucino\n(010)Oreo Shake:"))
	if x5=="001":
		print("You selected code 001: Cold Coffee")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Items:\nCold Coffee  - Rs.",coffee,"(Amount excluding 5% GST)")

	elif x5=="002":
		print("You selected code 002: Croissant")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Items:\nCroissant  - Rs.",croi,"(Amount excluding 5% GST)")

	elif x5=="003":
		print("You selected code 003: Cappucino")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Items:\nCappucino  - Rs.",capp,"(Amount excluding 5% GST)")

	elif x5=="004":
		print("You selected code 004: Mocha ")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Items:\nMocha  - Rs.",moch,"(Amount excluding 5% GST)")

	elif x5=="005":
		print("You selected code 005: Hot Chocolate")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Items:\nHot Chocolate  - Rs.",hot,"(Amount excluding 5% GST)")

	elif x5=="006":
		print("You selected code 006: Iced Vaniila")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Items:\nIced Vanilla  - Rs.",iced,"(Amount excluding 5% GST)")

	elif x5=="007":
		print("You selected code 007: Brownie")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Items:\nBrownie  - Rs.",brow,"(Amount excluding 5% GST)")

	elif x5=="008":
		print("You selected code 008: Kitkat Shake")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Items:\nKitkat Shake  - Rs.",kitkat,"(Amount excluding 5% GST)")

	elif x5=="009":
		print("You selected code 009: Frappucino")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Items:\nFrappucino  - Rs.",frapp,"(Amount excluding 5% GST)")

	elif x5=="010":
		print("You selected code 010: Oreo Shake")
		print("-"*50)
		print("Welcome to koffeegasm!")
		print("-"*50) 
		print("Items:\nOreo Shake  - Rs.",oreo,"(Amount excluding 5% GST)")

	else:
		print("You selected wrong code!\nTry Again!")

	print("-"*50)
	print("Thank you!\nVisit us again!\nRegards Team Koffeegasm!")
	print("-"*50)

else:
	print("You selected wrong input or probably entered wrong security code!\nTry Again!")
	print("-"*50)
	print("Thank you!\nVisit us again!\nRegards Team Koffeegasm!")
	print("-"*50)


