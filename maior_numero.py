num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))


# if num1 == num2 == num3:
#     print("Os tres numeros sao iguais.")
# else:
#     if num1 >= num2 and num1 >= num3:
#         maior = num1
#     elif num2 >= num1 and num2 >= num3:
#         maior = num2
#     else:
#         maior = num3

#     if num1 <= num2 and num1 <= num3:
#         menor = num1
#     elif num2 <= num1 and num2 <= num3:
#         menor = num2
#     else:
#         menor = num3
#     print(f"O maior numero e {maior} e o menor numero e {menor}.")

if num1 == num2 == num3:
    print("Os tres numeros sao iguais.")
else:
    print(f"O maior numero e {max(num1,num2,num3)} e o menor numero e {min(num1,num2,num3)}.")

    





