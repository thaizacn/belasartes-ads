lista_fibonacci = [1,1]

def fibonacci(repeat, contador = 0,  soma = lista_fibonacci[-1] + lista_fibonacci[-2]):
    lista_fibonacci.append(soma)
    contador += 1
    if contador == repeat:
        print(lista_fibonacci)
    else:
        fibonacci(repeat, contador, (lista_fibonacci[-1] + lista_fibonacci[-2]))
    
fibonacci(5)

def fibonacci(repeat, contador = 0, lista_fibonacci = [1,1]):
    lista_fibonacci.append(lista_fibonacci[-1] + lista_fibonacci[-2])
    contador += 1
    if contador == repeat:
        return lista_fibonacci
    
    return fibonacci(repeat, contador, lista_fibonacci)
    
print(fibonacci(5))