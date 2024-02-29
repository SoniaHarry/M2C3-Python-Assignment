import math

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

index_list= len(sale_prices)
list_sorted= sorted(sale_prices)

print (list_sorted)
firslist= list_sorted[:math.floor(index_list/2)]
print (firslist)

lastlist= list_sorted[math.floor(index_list/2)+1:]
print (lastlist)

media=list_sorted[math.floor(index_list/2):math.floor(index_list/2)+1]
print(media)

