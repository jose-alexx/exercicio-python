# Seleção if-else

print("Digite a nota 1: ")
nota__1 = float(input())

print("Digite a nota 2: ")
nota__2 = float(input())

media = ((nota__1 + nota__2) / 2)

if media >= 7.0 :
    print("O aluno foi aprovado com media " + str(media))
else :
    print(f"O aluno foi aprovado com media {str(media)}, deve fazer a prova final")

# Algoritimo - multiplo de 2, 3, 5 ou outro

print("Digite um numero")
num = int(input())

if num % 2 == 0 :
    print("O numero " + str(num) + " eh multiplo de 2")
elif num % 3 == 0 :
    print("O numero " + str(num) + " eh multiplo de 3")
elif num % 5 == 0 :
    print("O numero " + str(num) + " eh multiplo de 5")
else :
    print("O numero " + str(num) + " não eh multiplo de 2, 3 e 5")
    


