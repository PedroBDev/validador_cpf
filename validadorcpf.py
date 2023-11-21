import re 
import sys

entrada = input('Informe seu cpf:')
#Limpando as str do número:
cpf= re.sub(r'[^0-9]', '', entrada)

#verificando se é sequencial:
entrada_sequencial=entrada == entrada[0]*len(entrada)
if entrada_sequencial:
    print('Você digitou caracteres sequenciais.')
    sys.exit()

numeros_conta= cpf[:9]
i=1
multiplicador=10
soma=0
resto_soma=0

#FAZENDO A CONTA DA VERIFICAÇÃO:
for a in numeros_conta:
    if multiplicador>=2:
       soma=(int(a)*multiplicador)+soma        
    multiplicador-=1
digito_1=(soma*10)%11


#GERANDO 1° NÚMERO:
digito_1= digito_1 if digito_1<10 else 0

#GERAR SEGUNDO DÍGITO:

#ADICIONANDO O PRIMEIRO DÍGITO A LISTA:
numeros_conta_2=numeros_conta+str(digito_1)

#MULTIPLICADOR 2:
multiplicador_2=11
soma_2=0
#CÁLCULO DOS NÚMEROS
for a in numeros_conta_2:
    if multiplicador_2>=2:
       soma_2=(int(a)*multiplicador_2)+soma_2        
    multiplicador_2-=1
digito_2=(soma_2*10)%11

digito_2= digito_2 if digito_2<10 else 0

#VALIDANDO CPF:

#CPF GERADO:
cpf_gerado= numeros_conta+str(digito_1)+str(digito_2)

#VALIDANDO CPF:
if cpf_gerado==cpf:
    print('O cpf é válido')
else:
    print('O cpf é inválido')