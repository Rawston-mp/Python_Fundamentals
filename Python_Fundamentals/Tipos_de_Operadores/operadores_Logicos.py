# AND = para ser True, todos tem que ser True
#  OR = para ser True, basta um ser True


print(True and True)
print(True and False)
print(True or True)
print(True or False)
saldo = 100

saque = 250
limite = 200
conta_especial = True


exp = saldo >= saldo and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saldo and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

Conta_normal_com_saldo_suficiente = saldo >= saldo and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = Conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(exp_3)
