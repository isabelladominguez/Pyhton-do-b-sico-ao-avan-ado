custo_de_fabrica = float(input('Informe o custo de fábrica R$: '))

if custo_de_fabrica <= 12_000:
    custo_consumidor = custo_de_fabrica + (0.05 * custo_de_fabrica)
elif custo_de_fabrica <= 25_000:
    custo_consumidor = custo_de_fabrica + (0.25 * custo_de_fabrica)
else:
    custo_consumidor = custo_de_fabrica+ (0.35 * custo_de_fabrica)

print(f'Custo ao consumidor: R$ {custo_consumidor: .2f}')
