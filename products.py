import os # operating system

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價錢' in line:
				continue #跳到下一個迴圈
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q': #quit 逃出
			break
		price = input('請輸入商品價錢: ')
		products.append([name, price])
	print(products)
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		#print(p[0]) #只印出名字
		print(p[0], '的價錢是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價錢\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

#主程式
def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案在不在
		print('yeaah! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案...')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()