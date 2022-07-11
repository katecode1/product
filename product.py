import os #operating system
#讀取檔案
products = []
if os.path.isfile('products.csv'):#檢查檔案在不在
	print('yeah! Find it !') #找到檔案
	with open ('products.csv', 'r', encoding= 'utf-8') as f: 
		for line in f:
			if 'product,price' in line:
				continue
			product, price = line.strip().split(',')
			products.append([product, price])
	print(products)
else:
	print('No.....') #找不到檔案
#讓使用者輸入
while True:
	name = input('product of item : ')
	if name == 'q':
		break
	price = input('price of item : ')
	products.append([name, price])
print(products)	
#輸出檔案
for p in products:
	print(p[0],'price is', p[1])
with open('products.csv','w',encoding= 'utf-8') as f:
	f.write('product' + ',' + 'price' + '\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
