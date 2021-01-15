products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
	    break
	price = input('請輸入商品價格:')
	p = [] # 7~9裝小清單
	#p.append(name)
	#p.append(price)
	#p = [name,price]
	products.append([name, price]) # 小清單裝進大清單
	#products.append(name)
print(products)

products[0][0]