import os
from func_fornecedores import *

def menu_func():
  os.system('cls')
  print("=" * 50)
  print("SISTEMA ENGINSTOCK")
  print("-" * 50)
  print("FORNECEDORES:")
  print("1 - Cadastrar um fornecedor")
  print("2 - Atualizar um fornecedor")
  print("3 - Deletar um fornecedor")
  print("4 - Lista de fornecedores")
  print("=" * 50)

def main():
  menu_func()

if __name__ == '__main__':
  main()