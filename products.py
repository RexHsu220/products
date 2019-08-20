products = []
while True:
	name = input('Please enter the name of the product: ')
	if name == 'q':
		break
	price = input('Please enter the price of the product: ')
	products.append([name, price]) #create a sub list and add name and price instantly to the sub list, then append this sublist with name and price into products list
print(products)

