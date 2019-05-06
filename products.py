products = []
while True:
	p_name = input('請輸入商品名稱: ')
	if p_name == 'q':
		break
	p_price = input('請輸入商品價格: ')
	products.append([p_name, p_price])

print(products)

for p in products:
	print('商品名稱: ', p[0], ' 價格是: ', p[1])