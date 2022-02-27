# Construção da função code() para codificar o texto
def code():
    text = input("Digite o texto a ser criptografado: ")
    cifra = ""
    for i in range(len(text)):
        # ORD retorna o código ASCI do caractere (soma-se um para criptografar)
        c = ord(text[i])+1
        # CHR retorna o caractere correspondente ao número
        cifra = cifra + chr(c)
    print(f"Texto criptografado: {cifra}")

# Construção da função decode() para decodificar o texto
def decode():
    text = input("Digite o texto a ser criptografado: ")
    cifra = ""
    for i in range(len(text)):
        # ORD retorna o código ASCI do caractere (subtrai-se um para descriptografar)
        c = ord(text[i])-1
        # CHR retorna o caractere correspondente ao número
        cifra = cifra + chr(c)
    print(f"Texto descriptografado: {cifra}")

# Construção da função main()
def main():
    # Controle de looping do programa
    loop = 1

    # Looping
    while loop == 1:
        # Escolha da operação (criptografar ou descriptografar)
        operacao = input("Para criptografar digite 'c', para descriptografar digite 'd': ")
        # Validando operação
        while operacao != "c" and operacao != "d":
            operacao = input("\nPara criptografar digite 'c', para descriptografar digite 'd': ")
        # Criptografar
        if operacao.lower() == "c":
            code()
        # Descriptografar
        else:
            decode()
        # Looping
        loop = int(input("\nPara executar novamente digite '1', para finalizar digite '0': "))
        print()

# Chamada da função main()
main()
