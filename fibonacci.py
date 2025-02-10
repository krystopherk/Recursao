import turtle

# Função para desenhar um arco de círculo baseado na sequência de Fibonacci
def arco_fibonacci(t, raio, angulo):
    t.circle(raio, angulo)

# Função para desenhar a espiral de Fibonacci
def espiral_fibonacci(num_lados):
    t = turtle.Turtle()
    t.speed(10)
    
    # Inicializando os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    for i in range(num_lados):
        # Desenha um arco com o raio correspondente ao número de Fibonacci
        arco_fibonacci(t, b * 3, 90) 
        a, b = b, a + b  # Avança na sequência de Fibonacci
    
    turtle.done()

espiral_fibonacci(12)