import os #operating system
#讀取檔案
def read_file(filename):
	products = []
	with open (filename, 'r', encoding= 'utf-8') as f: 
		for line in f:
			if 'product,price' in line:
				continue
			product, price = line.strip().split(',')
			products.append([product, price])
	print(products)
	return products


#讓使用者輸入
def user_input(products):
	while True:
		name = input('product of item : ')
		if name == 'q':
			break
		price = input('price of item : ')
		products.append([name, price])
	print(products)	
	return products

#印出購買紀錄
def print_product(products):
	for p in products:
		print(p[0],'price is', p[1])


#輸出檔案
def write_file(filename, products):
	with open(filename,'w',encoding= 'utf-8') as f:
		f.write('product' + ',' + 'price' + '\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


#程式碼進入點
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):#檢查檔案在不在
			print('yeah! Find it !') #找到檔案
			products = read_file(filename)
			products = user_input(products)
			print_product(products)
			write_file(filename, products)
	else:
			print('No.....') #找不到檔案
#執行
main()


