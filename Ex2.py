print("Insert a string:")
str=input()
l=len(str)
if l<2:
    out=""
else:
    out=str[0] + str[1] + str[l-2] + str[l-1]
#i caratteri hanno indice da 0 fino ad l-1
print("Output: %s" %(out))