"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

sales={
    "g":20,
    "f":42,
    "t":10,
    "o":12
}
#list_sales= sales.items()
#print(list(sales))
#print(len(list(sales))-1)
#print(list_sales)
#print(len(list_sales))

for clave, valor in (sales.items()):
    content= valor*'$'
    print(clave + ' ' + content)