import os #作業系統(operating system)

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
		#跳過商品及價格
			if '商品,價格' in line:
				continue #繼續(重下一次迴圈執行)
			name, price = line.strip().split(',') #strip()去除\n , split('.')依"，"分割
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		p = []
		p.append(name)			#也可以寫為p = [name ,price]
		p.append(price)
		products.append(p)
		#上述7~11行，可簡寫成一行 products = [name ,price]
	print(products)
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1], '元')

#寫入檔案
#with為python獨有功能，可協助於執行完with裡程式碼後，自動關閉檔案。
#開啟的編碼為utf-8
def write_file(filename, products):	
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案是否存在
		print('此檔案存在!')
		products = read_file(filename)
	else:
		print('找不到檔案......')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()