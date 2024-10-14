class Configuracao:
    """Classe singleton para configuração."""

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Configuracao, cls).__new__(cls)
           
            cls._instancia.config = {}
        return cls._instancia

    def set_config(self, chave: str, valor: str) -> None:
        self.config[chave] = valor

    def get_config(self, chave: str) -> str:
        return self.config.get(chave, "Configuração não encontrada")


config1 = Configuracao()
config1.set_config("url", "http://exemplo.com")

config2 = Configuracao()
print(config2.get_config("url"))  
print(config1 is config2)  