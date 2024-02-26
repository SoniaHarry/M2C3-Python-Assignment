from functools import reduce

def function_exponencial (base, exponente):
    # list_calculos=[base]
    
    # for i in range(0,exponente-1):
    #     list=list_calculos.append(2)
    # return(list_calculos)
    list_calculos=[base]*exponente
    return reduce(lambda x, y:x*y , list_calculos)

print (function_exponencial(2,0))
# print(reduce(lambda x, y:x*y , function_exponencial(2,0)))
