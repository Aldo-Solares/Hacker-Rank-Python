
#LINK Este codigo no tiene link, El código busca el número faltante de una lista.

s = [1,2,3,4,5,7]
theorical_sum = ((len(s)+1)*(len(s)+2))/2
real_sum = sum(s)
print(int(theorical_sum - real_sum))