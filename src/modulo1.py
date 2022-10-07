from collections import namedtuple
import csv
import datetime

cricket = namedtuple("cricket", "Name, Team, Nationality, Matches, Bat_Runs, Bat_Average, Catches, Debut")

def lee_csv (ruta): 
    ''' Lee el fichero de entrada y devuelve una lista de audiencias
    
    ENTRADA: 
       - fichero: nombre del fichero -> str
    SALIDA: 
       - lista de audiencias -> [(int, float)] 

    Cada línea del fichero se corresponde con la audiencia de un programa,
    y se representa con una tupla con los siguientes valores:
        - edición
        - audiencia
    Hay que transformar la entrada (cadenas de caracteres) en valores numéricos
    para que puedan ser procesados posteriormente.
    '''
    datos = []    
    with open(cricket, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for Name, Team, Nationality, Matches, Bat_Runs, Bat_Average, Catches, Debut in f:
            Name = str(Name)
            Team = bool(Team)
            Matches = int(Matches)
            Bat_Runs = int(Bat_Runs)
            Bat_Average = float(Bat_Average)
            Catches = int(Catches)
            Debut = datetime.strptime(Debut)
            tupla = cricket(Name,Team,Nationality,Matches,Bat_Runs,Bat_Average,Catches,Debut)
            datos.append(tupla)
        return(datos)
cricket = lee_csv('./data/dataset1.csv')
print(cricket[:5])