from vid import Vid
from durazno import Durazno


def main():
    uva_1 = Vid('Uva Torrontés', 'Vino Torrontés')
    durazno_1 = Durazno('Durazno Flameo', 'Durazno en almíbar')
    print('=== PRUEBA DE INSTANCIACIÓN ===')
    print(uva_1)
    print(durazno_1)
    print('=== PRUEBA DE ENCAPSULAMIENTO ===')
    print(uva_1.fruto)
    print(uva_1.derivado)
    print(durazno_1.fruto)
    print(durazno_1.derivado)
    print('=== PRUEBA DE HERENCIA ===')
    print(uva_1.riego())
    print(durazno_1.riego())
    uva_1.derivado = 'Dulce de uva'
    durazno_1.derivado = 'Durazno desecado'
    print(uva_1.derivado)
    print(durazno_1.derivado)
    print('=== PRUEBA DE CLASE VID ===')
    print(uva_1.fruto)
    print(uva_1.derivado)
    print(uva_1.riego())
    print(uva_1.floracion())
    print(uva_1.cosecha())
    print(uva_1.poda())
    print('=== PRUEBA DE CLASE DURAZNO ===')
    print(durazno_1.fruto)
    print(durazno_1.derivado)
    print(durazno_1.riego())
    print(durazno_1.floracion())
    print(durazno_1.cosecha())
    print(durazno_1.poda())

if __name__ == '__main__':
    main()
