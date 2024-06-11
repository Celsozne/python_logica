def fibonacci_sequence(n):
    # Verifica se o número de termos é válido
    if n <= 0:
        print("O número de termos deve ser um inteiro positivo.")
    else:
        # Inicializa a sequência com os dois primeiros termos
        sequence = [0, 1]
        while len(sequence) < n:
            # Adiciona o próximo termo à sequência
            sequence.append(sequence[-1] + sequence[-2])
        # Retorna a sequência até o número de termos solicitado
        return sequence[:n]

# Solicita o número de termos da sequência ao usuário
num_terms = int(input("Digite o número de termos da sequência de Fibonacci: "))

# Gera e imprime a sequência de Fibonacci
fibonacci_sequence_result = fibonacci_sequence(num_terms)
print("Sequência de Fibonacci:", fibonacci_sequence_result)
