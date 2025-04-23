from typing import Optional


class Produto:
    #__init__ é método construtor de uma classe python
    def __init__(self, nome: str, id: Optional[int] = None):
       self.nome = nome 
       self.id = id



# # variaável
# nome = "Francisco"
# #
# # nome_objeto = instanciando um objeto da classe Produto, como eu sei disso ? pq é feito Produto(...)
# uva = Produto("Uva verde")



# if __name__ == "__main__":
#     salgadinho = Produto(nome="salgadinho")
#     print(salgadinho)

