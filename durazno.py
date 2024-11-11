from frutal import Frutal

class Durazno(Frutal):
    def __init__(self, fruto, derivado):
        super().__init__(fruto, derivado)

    def riego(self):
        return 'Regar cada 4, 6 ó 9 días dependiendo el terreno.'
    
    def floracion(self):
        return 'Florece en primavera.'
    
    def cosecha(self):
        return 'Se cosecha de enero a abril.'
    
    def poda(self):
        return 'Se poda en finales junio o julio.'
