# Implemente uma função em Python que calcule o n-ésimo número da sequência de Fibonacci.

n = int(input('Digite um número inteiro maior ou igual a 2: \n'))  # não vou tratar neste caso o erro de receber um n < 2

def seq_fibonacci(n):
    s1 = 0      # primeiro número definido
    s2 = 1      # segundo número definido

    if n == 2:
        return f'{s1}, {s2}'

    fibonacci_seq = [s1, s2]
    for i in range(2, n):
        next_number = fibonacci_seq[i-1] + fibonacci_seq[i-2]
        fibonacci_seq.append(next_number)

    return ', '.join(map(str, fibonacci_seq))

print(seq_fibonacci(n))
