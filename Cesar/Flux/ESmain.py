from menus import *

menu_inicial()

escolha = int(input())

while escolha != 4:
  if escolha == 1:
    menu_gerenciar_estoque()
  elif escolha == 2:
    menu_controle_estoque()
  elif escolha == 3:
    menu_inicial()
  
  escolha = int(input())

print('volte sempre')