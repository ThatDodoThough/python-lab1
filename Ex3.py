riga1 = """Insert the number corresponding to the action
you want to perform:\n"""
riga2 = "\t1. insert a new task;"
riga3= "\t2. remove a task;"
riga4= "\t3. show all the tasks;"
riga5= "\t4. close the program.\n\nYour choice:"
lista=[]
N=0

scelta = 0
while scelta!=4:
    print(riga1)
    print(riga2)
    print(riga3)
    print(riga4)
    print(riga5)
    str = input()
    scelta = int(str)
    if scelta==1:
        print("Inserire nuovo task: ",end='')
        nuovo=input()
        lista.append(nuovo)
        N=N+1
    elif scelta==2:
        print("Inserire il task da rimuovere: " ,end='')
        nuovo=input()
        #lista.pop(1)
        lista.remove(nuovo)
        N=N-1
    else:
        for elem in lista:
            print(elem)
print("Fine")

#due modi di togliere elementi dalla lista. Uno dipende da
#indice, l'altro prende direttamente l'elemento