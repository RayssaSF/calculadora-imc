nome=input("Digite seu Nome: ")
print("Seja Bem Vinda",nome,"Vamos Calcular seu Indice de Massa Corporal")

peso=float(input("Digite o seu Peso Atual: ")) #usar ponto exemplo 73.50
altura=float(input("Digite a sua Altura: ")) #usar ponto exemplo 1.50

imc = peso / (altura**2)

if(imc < 16.9):
    print("Muito abaixo do Peso")
elif(imc>= 17) and (imc<18.4):
    print("Abaixo do Peso")
elif(imc<=18.5) and (imc<24.9):
    print("Peso Normal")
elif(imc<=25) and  (imc<29.9):
    print("Acima do Peso")
elif(imc<=30) and (imc<34.9):
    print("Obesidade Grau I ")
elif (imc<=35) and (imc<40):
    print(" Obesidade Grau II")
else:
    print("Obesidade Grau III")