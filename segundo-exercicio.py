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

# if aninhado

print("Digite o valor 1: ")
valor__1 = int(input())

print("Digite o valor 2: ")
valor__2 = int(input())

print("Digite o valor 3: ")
valor__3 = int(input())

if (valor__1 >= valor__2) :
    if (valor__1 >= valor__3) :
        print(f"o valor {valor__1} eh o maior de todos")
    else :
        print(f"o valor {valor__3} eh o maior de todos")

    if (valor__2 >= valor__3) :
        print(f"o valor {valor__2} eh o maior de todos")
    else : 
        print(f"o valor {valor__3} eh o maior de todos")


