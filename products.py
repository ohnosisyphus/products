# 讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價錢' in line:
			continue #跳到下一個迴圈
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quit 逃出
		break
	price = input('請輸入商品價錢: ')
	products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
	#print(p[0]) #只印出名字
	print(p[0], '的價錢是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價錢\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')