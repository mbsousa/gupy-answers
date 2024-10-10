# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, 
# além de informar a quantidade de vezes em que ela ocorre.


def quantidade(palavra):
    contagem = palavra.lower().count('a')

    if contagem > 0:
        resposta = f'A palavra -{palavra}- possui a letra "a" {contagem} vez(es).'
    else:
        resposta = f'A palavra -{palavra}- não possui a letra "a".'

    return resposta

def main():
    word = input("Digite uma palavra: ")
    resultado = quantidade(word)
    print(resultado)

if __name__ == '__main__':
    main()
