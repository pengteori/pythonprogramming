def buy(a):
    print('[구입]')
    item = input('상품명? ')
    if item == '':
        return False
    quantity = int(input('수량은? '))
    shopping_bag[item] = quantity
    print(f'장바구니에 {item} 가(이) {quantity}개 담겼습니다.')

def show(a):
    print('>>>장바구니 보기:', shopping_bag)

def find(a):
    while True:
        item = input('장바구니에서 확인하고자 하는 상품은? ')
        if item == '':
            break
        quantity = shopping_bag[item]
        if item in shopping_bag:
            print(f'{item} 은(는) {quantity}개 담겨 있습니다.')

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
