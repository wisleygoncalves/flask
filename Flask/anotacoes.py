"""
Classes:

class Funcionarios():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def dados(self):
        return {'nome': self.nome, 'salário': self.salario}

Herança:
class Admin():
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def atualizar_dados(self, nome):
        self.nome = nome
        return self.dados()

Args e kwargs
    def teste(*args, **kwargs)

- Args é uma tupla e recebe múltiplos parâmetros
- kwargs é dicionário e recebe múltiplos parâmetros
"""
