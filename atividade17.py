# Exercício Python 17: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.

ano=int(input("ano de nascimento :"))
anoatual=int(input("ano atual: "))
idade=anoatual-ano
if idade < 18:
    print(f"ainda à se alistar, daqui a {18-idade} anos")
elif idade == 18:
    print(f"você tem {idade} agora é o momento de se alistar")
else:
    print(f"você já deveria ter se alistado a {idade-18} anos")