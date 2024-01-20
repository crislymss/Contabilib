from matplotlib import pyplot as plt

def criar_grafico(self, dados):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(dados)), list(dados.values()), align='center')
    plt.xticks(range(len(dados)), list(dados.keys()))
    plt.savefig('grafico.png')
