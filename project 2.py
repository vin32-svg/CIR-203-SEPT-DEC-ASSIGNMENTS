routes=["maseno-kisumu","kisumu-kericho","siaya-nairobi","kakamega-Nakuru","Bungoma-Naivasha","kisii-kericho","Nyamira-Kiambu","kericho-Nairobi","Narok-Kericho","cheptull-Bomet",]
print(routes)
routes.append("Eldoret_Narok")
print(routes)
routes.remove("maseno-kisumu")
print(routes)
routes.sort()
print(routes)
routes.reverse()
print(routes)
count_n = sum(1 for r in routes if r.startswith("N"))
print("\n routes starting with N",count_n)
long_routes =[(r for r in routes if len(r)>10)]
print("\nlong_routes",long_routes)
