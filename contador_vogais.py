frase = str(input("Digite uma frase: ")).lower()
vogais = "aeiou"
contador = 0
# a = 0
# e = 0
# i = 0
# o = 0
# u = 0
contagem = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}


for letra in frase:
    if letra in vogais:
        # if letra == "a":
        #     a += 1
        # elif letra == "e": 
        #     e += 1
        # elif letra == "i":
        #     i += 1
        # elif letra == "o":
        #     o += 1
        # elif letra == "u":
        #     u += 1
        # contador += 1
        contagem[letra] += 1
    
total = sum(contagem.values())    

print(f"A frase digitada possui {total} vogais.")    

for v, qtd in contagem.items():
    print(f"{v.upper()}: {qtd}")


# print(f"A frase digitada possui {contador} vogais. Sendo: A: {a}, E: {e}, I: {i}, O: {o}, U: {u}.")