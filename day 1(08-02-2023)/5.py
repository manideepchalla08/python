def bakery_sale(loaves):
    regular_price=185*loaves
    discount=0.6*regular_price
    total_price=regular_price-discount
    return regular_price,discount,total_price
loaves=int(input("entre the number of loaes of day old bread:"))
regular_price,discount,total_price=bakery_sale(loaves)
print("regular price:{:.2f}rupees",format(regular_price))
print("discount:{:.2f}rupees",format(discount))
print("total_price:{:.2f}rupees",format(total_price))
