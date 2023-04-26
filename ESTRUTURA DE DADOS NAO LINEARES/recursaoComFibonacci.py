import decimal 

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

dia_aniversario = decimal.Decimal(input('Qual o dia do seu aniversário? '))
mes_aniversario = decimal.Decimal(input('Qual o mês do seu aniversário (número)? '))

n = dia_aniversario + mes_aniversario
fibonacci_n = fibonacci(n)
print(f"O {n}º termo da série de Fibonacci é {fibonacci_n}.")