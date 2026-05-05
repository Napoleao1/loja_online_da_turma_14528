class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco
        
        
        
        
    def get_preco(self):
        return self._preco 
    
    
    
    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço: R$ {self._preco}")
        
        
        
    def aplicar_desconto(self, percentual):
        if percentual  >= 0 and percentual <= 100:
            self._preco -= self._preco * (percentual / 100)
        else:
            print("desconto invalido")