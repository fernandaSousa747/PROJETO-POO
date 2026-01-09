from datetime import date


class Jogo:
    def __init__(self, titulo, genero, horas_jogadas=0):
        self.titulo = titulo
        self.genero = genero
        self._horas_jogadas = 0
        self.status = "NÃO INICIADO"
        self.data_inicio = None
        self.data_fim = None
        self.horas_jogadas = horas_jogadas

    
    @property
    def horas_jogadas(self):
        return self._horas_jogadas

    @horas_jogadas.setter
    def horas_jogadas(self, valor):
        if valor < 0:
            raise ValueError("Horas jogadas não podem ser negativas.")
        self._horas_jogadas = valor

    def iniciar(self):
        self.status = "JOGANDO"
        self.data_inicio = date.today()

    def finalizar(self):
        if self.horas_jogadas < 1:
            raise ValueError("Não é possível finalizar um jogo com menos de 1 hora jogada.")
        self.status = "FINALIZADO"
        self.data_fim = date.today()

    # Métodos especiais
    def __str__(self):
        return f"{self.titulo} ({self.genero}) - {self.status}"

    def __repr__(self):
        return f"Jogo(titulo='{self.titulo}', genero='{self.genero}', horas={self.horas_jogadas})"

    def __eq__(self, other):
        return self.titulo == other.titulo and self.genero == other.genero

    def __lt__(self, other):
        return self.horas_jogadas < other.horas_jogadas



class JogoPC(Jogo):
    def __init__(self, titulo, genero, horas_jogadas=0, loja="Steam"):
        super().__init__(titulo, genero, horas_jogadas)
        self.loja = loja


class Colecao:
    def __init__(self, nome):
        self.nome = nome
        self.jogos = []

    def adicionar_jogo(self, jogo):
        if jogo in self.jogos:
            raise ValueError("Jogo já existe na coleção.")
        self.jogos.append(jogo)

    def remover_jogo(self, jogo):
        self.jogos.remove(jogo)

    def listar_jogos(self):
        return self.jogos

    def __str__(self):
        return f"Coleção '{self.nome}' com {len(self.jogos)} jogos"


# Exemplo de uso
if __name__ == "__main__":
    jogo1 = JogoPC("The Witcher 3", "RPG", 10)
    jogo1.iniciar()
    jogo1.finalizar()

    colecao = Colecao("Favoritos")
    colecao.adicionar_jogo(jogo1)

    print(jogo1)
    print(colecao)
