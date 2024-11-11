from frutal import Frutal


class Vid(Frutal):
    def __init__(self, fruto, derivado):
        super().__init__(fruto, derivado)
        
    def riego(self):
        return 'Regar una a dos veces por semana.'
    
    def floracion(self):
        return 'Florece entre octubre y noviembre.'
    
    def cosecha(self):
        return 'Finales de enero para variedades blancas y finales de febrero para tintas.'
    
    def poda(self):
        return 'Se poda de mayo a agosto.'
