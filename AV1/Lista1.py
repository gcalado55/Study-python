#Questão 1
print ('Olá UNINASSAU!')

#Questão 2
num = float(input('Digite um numero: '))
print ('O numero informado foi' ,num)

#Questão 3
print ('Digite dois números')
num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))
sum = num1 + num2
print ('Soma =',sum)

#Questão 4
print('Insira as notas do aluno')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
avg = (nota1 + nota2 + nota3 + nota4)/4
print('A média final é:', avg)

#Questão 5
metros = float(input('Digite o valor em metros: '))
centimetros = metros*100
print ('Valor em centimetros =',centimetros)

#Questão 6
import math
raio = float(input('Raio da circunferência: '))
area = math.pi * raio * raio
txt = 'Área: {:.1f}'
print (txt.format(area))

#Questão 7
lado = float(input('Lado do quadrado: '))
dobroArea = lado * lado * 2
print('dobro do lado = ',dobroArea)

#Questão 8
horas = float(input('Horas trabalhadas: '))
precoPorHora = float(input('Preço da hora: '))
salario = horas * precoPorHora
print('Salario(Mês):', salario)

#Questão 9
num = float(input('Digite um número: '))
if(num < 0):
    print('Negativo')
elif(num > 0):
    print('Positivo')

#Questão 10
while True:
 sexo = input("\nDigite \nF - Feminino\nM - Masculino\n")
 sexo = sexo.upper()
 if sexo == "F":
  print("\nVocê escolheu Feminino\n")
  break
 elif sexo == "M":
  print("\nVocê escolheu Masculino\n")
  break
 else:
  print("\nSexo invalido")