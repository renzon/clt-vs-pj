def imposto_de_renda(salario_anual):
    """
    Calcula imposto de renda PF de acordo com faixa do ano de 2019
    https://impostoderenda2019.net.br/tabela-imposto-de-renda-2019/

    """
    saldo = salario_anual
    aliquotas_faixas = {0.275: 55_976.16, 0.225: 45_012.60, 0.15: 33_919.80, 0.075: 22_847.76, 0: 0}
    ir = 0
    desconto_simplificado = 0.25  # 25% de desconto simplificado
    for aliquota, faixa in aliquotas_faixas.items():
        delta = max(saldo - faixa, 0)
        ir += delta * aliquota * (1 - desconto_simplificado)
        saldo = min(saldo, faixa)
    return ir


for salario_anual in reversed([22_847.76, 33_919.80, 45_012.60, 55_76.16, 100_000]):
    print(imposto_de_renda(salario_anual))
