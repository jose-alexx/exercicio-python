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



