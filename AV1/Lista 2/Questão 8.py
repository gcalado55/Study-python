from termcolor import colored

print(colored("Calculo IMC:", attrs = ['bold']))
Peso = float(input("Digite seu peso(Kg): "))
ALtura = float(input("Digite sua altura(cm): "))

def conversorDeAltura():
    ALturaM = ALtura/100
    return ALturaM

AlturaMetros = conversorDeAltura()

def CalculoImc():
    imc = Peso / AlturaMetros ** 2
    return imc

imc = CalculoImc()

print ("\n Seu IMC é %.2f" % imc)
    