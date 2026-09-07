# Calculadora de Consumo Elétrico
print("=======================================")
print(" Energy Quest - Calculadora de Consumo")
print("=======================================")

# Entrada de dados aparelho
input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))

# Valor da energia elétrica
valor_kwh = 0.65

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo do custo mensal
custo_mensal = consumo_mensal * valor_kwh

# Resultado
print("\n====================================")
print(" RESULTADO")
print("====================================")
print(f"Consumo mensal: {consumo_mensal:.2f} kWh/mês")
print(f"Custo mensal: R$ {custo_mensal:.2f}/mês")
