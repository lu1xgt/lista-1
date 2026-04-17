dias = int(input("digite uma quantidade de dias: "))
horas = int(input("digite uma quantidade de horas: "))
minutos = int(input("digite uma quantidade de minutos: "))
segun = int(input("digite uma quantidade de segundos: "))

segunDia = (dias * 86400)
segunHora = (horas * 3600)
segunMinu = (minutos * 60)

segundos = (segun + segunMinu + segunHora + segunDia)

print(f"o total em segundos é {segundos}")