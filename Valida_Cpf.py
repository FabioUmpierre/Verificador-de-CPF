cpf = input("Digite um CPF válido: ")
calculo = 0
contador= 10
novo_cpf = cpf[0:-2] # pega os 9 primeiros digitos do cpf


for indice in range (9):
    calculo += int(cpf[indice]) * contador # multiplica os 9 primeiros digitos do cpf com os numeros de 10 até 2 e depois soma
    contador -= 1 # contador reverso
    d =  11 - (calculo % 11) # gera o penultimo digito
    if d > 9:
        d = 0
novo_cpf += str(d) # adiciona o penultimo digito ao cpf comparativo
calculo = 0
contador = 11

for indice in range(10):
    calculo += int(cpf[indice]) * contador # multiplica os 10 primeiro digitos do cpf com os numeros de 11 até 2 e depois soma
    contador -= 1
    d = 11 - (calculo % 11) # gera o ultimo digito
novo_cpf += str(d)
sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf) # verifica se existe sequencia


if cpf == novo_cpf and not sequencia: # verifica se os cpfs são iguais, se forem, o cpf digitado é válido
    print('Válido')
else:
    print('Inválido')







