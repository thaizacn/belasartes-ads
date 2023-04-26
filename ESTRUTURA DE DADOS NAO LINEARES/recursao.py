def recursaoSoma(num1, num2, soma):
    
    
    if num1 == num2:
        print(soma + num2)
    else:
        recursaoSoma(num1 + 1, num2, soma + num1)

recursaoSoma(2,5,0)