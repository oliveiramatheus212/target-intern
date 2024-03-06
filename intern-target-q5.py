def inverter_string(s):
    resultado = ""
    
    for i in range(len(s)-1, -1, -1):
        resultado += s[i]
    
    return resultado

# Exemplo de uso
entrada = input("Digite uma string: ")
resultado_invertido = inverter_string(entrada)

print("String original:", entrada)
print("String invertida:", resultado_invertido)