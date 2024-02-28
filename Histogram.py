"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

sales={
    "google":20,
    "facebook":42,
    "twitter":10,
    "offline":12
}
#list_sales= sales.items()
#print(list(sales))
#print(len(list(sales))-1)
#print(list_sales)
#print(len(list_sales))

for clave, valor in (sales.items()):
    print(clave[0] + ' ' + valor*'$')