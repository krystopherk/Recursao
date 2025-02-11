import turtle

def espiral_fibonacci_recursiva(t, a, b, num_lados):
    if num_lados == 0:  # Caso base: quando não há mais lados para desenhar
        return
    
    t.circle(b * 3, 90)  # Desenha um arco com o raio correspondente ao número de Fibonacci
    
    # Chamada recursiva para o próximo arco na sequência
    espiral_fibonacci_recursiva(t, b, a + b, num_lados - 1)

# Configuração inicial
t = turtle.Turtle()
t.speed(10)

# Chamada da função recursiva
espiral_fibonacci_recursiva(t, 0, 1, 12)

turtle.done()
