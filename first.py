# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(n):
    t1, t2 = 0, 1
    print(t1, t2, end=', ')

    if n == t1 or n == t2:
        print(f'O número {n} pertence à sequência.')
        return

    while True:
        calculo = t1 + t2
        print(calculo, end=', ')
        
        if calculo == n:
            print(f'\nO número {n} pertence à sequência.')
            return
        if calculo > n:
            print(f'\nO número {n} não pertence à sequência.')
            return

        t1, t2 = t2, calculo

def main():
    n = int(input("Digite um número: "))
    fibonacci(n)

if __name__ == '__main__':
    main()
