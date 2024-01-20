def calcular_rescisao(self, funcionario_id, salario, tempo_servico, motivo_rescisao):
       # Esta é apenas uma função de exemplo. A lógica real dependerá das leis trabalhistas do seu país.
        if motivo_rescisao == "demissao":
            return salario * 0.5
        elif motivo_rescisao == "aposentadoria":
            return salario * tempo_servico * 0.01
        else:
            return 0
