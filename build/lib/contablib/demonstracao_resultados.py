def demonstracao_resultados(self):
    receitas = sum(transacao["valor"]
                   for transacao in self.transacoes if transacao["categoria"] == "Receita")
    despesas = sum(transacao["valor"]
                   for transacao in self.transacoes if transacao["categoria"] == "Despesa")
    lucro = receitas - despesas
    return receitas, despesas, lucro
