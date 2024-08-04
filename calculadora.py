#Exemplo 1: Calculadora de IMC

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))
             
imc = peso / (altura ** 2)
print("Seu IMC é: ", imc)

# Operações aritimetricas

numero__1 = int(input("Digite o primeiro numero: ")) # 5
numero__2 = int(input("Digite o segundo numero: ")) # 2

soma = numero__1 + numero__2
subtracao = numero__1 - numero__2
multiplicacao = numero__1 * numero__2
divisao = numero__1 / numero__2
divisao_inteira = numero__1 // numero__2
modulo =numero__1 % numero__2
exponenciacao = numero__1 ** numero__2

print(soma) # 7
print(subtracao) # 3
print(multiplicacao) # 10
print(divisao) # 2.5
print(divisao_inteira) # 2
print(modulo) # 1
print(exponenciacao) # 25