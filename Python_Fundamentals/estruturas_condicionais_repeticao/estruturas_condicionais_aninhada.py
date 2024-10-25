conta_normal = True
Conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo +  cheque_especial):
        print("Saque realizado com uso do cheque especia!")
    else:
        print("Saque não realizado, saldo insuficiente!")
elif Conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
