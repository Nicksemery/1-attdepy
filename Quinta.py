# Crie um programa em Python em que as quatro operações em que todos os resultados resultam em 8.
# confuso, o resultado final é 8 ou tem que ter as quatro operações com resultado 8?
#%%
# primeiro sendo o resultado final 8
n1 = float(input("digite um numero: "))
n2 = n1 * 0
n3 = n2 /2
n4 = n3 - n2 - n1
soma = (n1 + n2 + n3 + n4) + 8
print (soma)
#%%
# segundo como cada operação dando 8
n1 = float(input("digite um numero: "))
n2 = (n1 *0) +8
n3 = (n1 /1 -n1) +8
n4 = (n2 -n3) +8
n5 = (n3 + n4) -n2 *2 + 8
print (n2, n3, n4, n5)