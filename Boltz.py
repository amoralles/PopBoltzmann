import numpy as np

def Popi(txt):
    # Carrega dados do arquivo
    data = np.loadtxt(txt)
    ee = data[:, 1]
    emin = np.min(ee)
    popi = np.zeros_like(ee)
    soma = 0.
    deltae = np.zeros_like(ee)
    RT = 8.3144621*298

    # Calcula as probabilidades
    for i in range(len(ee)):
        deltae[i] = (ee[i]-emin)*2.62456e6
        soma = soma + np.exp(-deltae[i]/RT)

    for i in range(len(ee)):
        popi[i] = np.exp(-deltae[i]/RT)/soma

    # Seleciona os 10 maiores valores de probabilidade
    top10_indices = np.argsort(popi)[-10:]
    top10_probabilidades = popi[top10_indices]
    top10_coluna1 = data[:, 0][top10_indices]

    # Retorna os valores
    return top10_coluna1, top10_probabilidades

# Exemplo de uso:
coluna1, probabilidades = Popi('Energias')
for c1, p in zip(coluna1, probabilidades):
    print('{}\t{}'.format(c1,p))
