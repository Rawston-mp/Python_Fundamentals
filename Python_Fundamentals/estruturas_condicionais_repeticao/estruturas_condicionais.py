MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade")
    
if idade < MAIOR_IDADE:
    print("Você é menor de idade")
    
    # *************************
    
if idade >= MAIOR_IDADE:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
    
    # *************************

if idade >= MAIOR_IDADE:
    print("Maior  de idade, pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode faxer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Menor de idade, não pode tirar CNH")
    
    # *************************
    


