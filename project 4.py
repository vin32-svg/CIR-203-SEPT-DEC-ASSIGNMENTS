dict = {
    "books": 25,
    "laptops": 8,
    "Tablets": 15,
    "desktops": 5,
    "Bags": 12
}
print("Initial dict:", dict)

dict["cables"] = 10
dict["books"] = 30
print("Updated dict:", dict)

def low_stock(dic):
    return {k: v for k, v in dic.items() if v < 10}

print("Products with low stock:", low_stock(dict))

del dict["desktops"]
print("After removing desktops:", dict)

for product, quantity in dict.items():
    print(product, ":", quantity)