def fatorial(n):
    #Caso base
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
print(f"O resultado é: {fatorial(5)}")
