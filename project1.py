print("...We are made for goodness & We are made for love...")
x=int(input("Enter Your Bike Mileage: "))
y=int(input("Enter Travel Kilometer: "))
z=int(input("Enter today 1 liter fuel price: "))

#To find the total liter for travel 
l=y//x
#To find the total cost for travel
p=z*l
#Average value
A=z/x

if(l>1):
	print("Total amount of fuel ", l,"litres")
	print("Total amount of cost ", p)
else:
	print("Total amount of fuel lesser then 1l")
	print("Total amount of Cost lesser then", z)
	
print("Average cost of fuel for 1km:", A)
print(" 'Have a wounderful Journey' ")

#Nice Project
