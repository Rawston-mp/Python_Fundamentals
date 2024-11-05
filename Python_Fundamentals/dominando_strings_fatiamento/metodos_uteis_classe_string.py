nome = "rAwsTOn"

print(nome.upper())   # imprime "RAWSOTON"

print(nome.lower())    # imprime "rawston"

print(nome.title())     # imprime "Rawston"


texto = "   Olá, mundo!   "


print(texto + ".")
print(texto.strip() + ".") # remove espaços em branco

print(texto.rstrip()  + ".") # remove espaços em branco da direita

print(texto.lstrip()  + ".") # remove espaços em branco da esquerda

menu = "python"
print(menu[0]) # imprime a primeira letra do menu
print(menu.center(10, "*")) # centraliza o texto e preenche com *
print("-".join(menu))  # junta as letras do menu com "-" entre elas
print("".join(menu))  # junta as letras do menu sem espaço entre elas
