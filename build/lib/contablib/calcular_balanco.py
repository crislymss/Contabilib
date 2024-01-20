def calcular_balanco(self):
    ativos = sum(transacao["valor"]
                 for transacao in self.transacoes if transacao["categoria"] == "Ativo")
    passivos = sum(transacao["valor"]
                   for transacao in self.transacoes if transacao["categoria"] == "Passivo")
    patrimonio_liquido = ativos - passivos
    return ativos, passivos, patrimonio_liquido
