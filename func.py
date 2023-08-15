n1 = float(input("Digite primeiro número: "))
n2 = float(input("Digite segundo número"))

def soma(n1,n2):
    global resultado
    resultado = n1 + n2

def subtrai(n1,n2):
    global resultado
    resultado = n1 - n2

def multiplica(n1,n2):
    global resultado
    resultado = n1 * n2

def divide(n1,n2):
    global resultado
    resultado = n1 / n2

opcao = input("ESCOLHA A OPÇÃO DESEJADA:\n+ => Somar\n- => Subtrair\n* => Multilpicar\n/ => Dividir\n")

if opcao == '+':
    soma(n1, n2)
elif opcao == '-':
    subtrai(n1, n2)
elif opcao == '*':
    multiplica(n1, n1)
elif opcao == '/':
    divide(n1, n2)

print("O resultado para os números digitados e {}".format(resultado))