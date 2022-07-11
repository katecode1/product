products = []

while True:
	name = input('product of item : ')
	if name == 'q':
		break
	price = input('price of item : ')
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price]
	products.append([name, price])
print(products)	

for p in products:
	print(p[0],'price is', p[1])