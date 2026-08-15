primeiro_numero = int(input("DIGITE UM NÚMERO: "))
segundo_numero = int(input("DIGITE OUTRO NÚMERO: "))

print(" SOMA = (1)\n SUBTRAIR = (2)")

pergunta_operadores = input("DIGITE O NÚMERO CORRESPONDENTE AO OPERADOR QUE DESEJA: ")

somar = primeiro_numero + segundo_numero
sub = primeiro_numero - segundo_numero

if pergunta_operadores in "1":
    print(f"RESULTADO DA SOMA {somar}")

elif pergunta_operadores in "2":
    print(f"RESULTADO DA SSUBTRAÇÃO {sub}")

else: 
    print("RESPOSTA INCORRETA")