from collections import namedtuple
import csv
from datetime import datetime

#Función para leer formato fecha y hora
def parse_date(cadena, formato = "%d/%m/%Y"):
    return datetime.strptime(cadena, formato).date()

def parse_time(cadena, formato = '%H:%M:%S'):
    return datetime.strptime(cadena, formato).time()

def parse_datetime(cadena, formato = '%d/%m/%Y-%H:%M:%S'):
    return datetime.strptime(cadena, formato)

#Función para leer formato booleano
def parse_bool(cadena):
    if cadena == 'CSK':
        booleano = True
    else:
        booleano = False
    return booleano

cricket = namedtuple("cricket", "Name, Team, Nationality, Matches, Bat_Runs, Bat_Average, Catches, Debut")
#Función para leer los datos del csv
def lee_csv(dataset1):
    datos = []    
    with open(dataset1, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for Name, Team, Nationality, Matches, Bat_Runs, Bat_Average, Catches, Debut in lector:
            Team = parse_bool(Team)
            Matches = int(Matches)
            Bat_Runs = int(Bat_Runs)
            Bat_Average = float(Bat_Average)
            Catches = int(Catches)
            Debut = parse_datetime(Debut)
            tupla = cricket(Name, Team, Nationality, Matches, Bat_Runs, Bat_Average, Catches, Debut)
            datos.append(tupla)
        return(datos)
datos = lee_csv("./data/dataset1.csv")
