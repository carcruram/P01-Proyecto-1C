from modulo1 import lee_csv
num_registros = 23

datos = lee_csv("./data/dataset1.csv")
def num_total (datos):
    datos = len(datos[num_registros])
    print('El número total de registros leídos es:', datos)
    return(datos)

def num_primeros(datos):
    datos = datos[:3]
    print('Los tres primeros registros leídos son:', datos)
    return(datos)

def num_ultimos(datos):
    datos = datos[(num_registros-4):]
    print('Los tres últimos registros leídos son:', datos)
    return(datos)

if __name__ == '__main__':
    print(datos[:num_registros])
    num_total(datos)
    num_primeros(datos)
    num_ultimos(datos)