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
