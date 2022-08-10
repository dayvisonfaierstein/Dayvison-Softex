# ATIVIDADE 2 - MODULO 2

rodas = int(input("Informe a quantidade de rodas do veículo: "))
peso = float(input("Infoerme o peso bruto em quilogramas do veículo: "))
qtdPessoas = int(input("informe a quantidade de pessoas no veículo: "))
if rodas <= 3 and rodas >= 2:
    print("O veículo é da categoria A")
elif rodas == 4 and qtdPessoas <= 8 and peso <= 3500:
    print("O veículo é da categoria B")
elif rodas >= 4 and qtdPessoas <= 8 and peso >= 3500 and peso <= 6000:
    print("O veículo é da categoria C")
elif rodas >=4 and qtdPessoas > 8 and peso >= 3500 and peso <= 6000:
    print("O veículo é da categoria D")
elif rodas >=4 and peso > 6000:
    print("O veículo é da categoria E")
else:
    print("Com as informações de quantidade de rodas", rodas, ", peso", peso, "e quantidade de pessoas", qtdPessoas, "não foi possível classificar seu veículo.")