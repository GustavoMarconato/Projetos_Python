print("Bem vindo a calculadora simples!")
operador = input("Escolha a operacao que deseja realizar: ") 
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if operador == "+":
    soma = num1 + num2
    print(f"A soma dos numeros e {soma}")
elif operador == "-":
    diferenca = num1 - num2
    print(f"A diferenca dos numeros e {diferenca}")
elif operador == "*":
    multiplicacao = num1 * num2
    print(f"A multiplacao dos numeros e {multiplicacao:.2f}")
elif operador == "/":
    if num2 != 0:
        quociente = num1 / num2
        print(f"O quociente dos numeros e {quociente:.2f}")
    else:
        print("Erro: divisao por zero nao e permitida")
else:
    print("O operador nao e valido")
