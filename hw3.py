def get_fixed_price(a,b):
    p=(b/(100-a))*100
    return p
disR=float(input("할인율은? "))
disPA=float(input("A상품의 할인된 가격은? "))
disPB=float(input("B상품의 할인된 가격은? "))
priceA=get_fixed_price(disR, disPA)
priceB=get_fixed_price(disR, disPB)
print("A상품의 정가는",priceA,"원")
print("B상품의 정가는",priceB,"원")
