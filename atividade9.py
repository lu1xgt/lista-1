quant = int(input("qauntos cigarros você fuma por dia?: "))
anos = int(input("a quantos anos você fuma?: "))

cigarrosFumados = ((anos * 365) * quant)
tempoPerdido = (((cigarrosFumados * 10) / 60) / 24)

print (f"você ja perdeu {tempoPerdido} dias por fumar")