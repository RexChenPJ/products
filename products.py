products = []

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