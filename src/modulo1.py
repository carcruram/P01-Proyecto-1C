import csv
cricket = namedtuple("cricket", "Name, Team, Nationality, Matches, Bat_Runs, Bat_Average, Catches, Debut")


def lee_csv (ruta): 
    datos = []    
    with open(cricket, encoding='utf-8') as f:
        lector =csv.reader(f, delimiter = ';')
        next(lector)
        for Name, Team, Nationality, Matches, Bat_Runs, Bat_Average, Catches, Debut in f:
            Team = bool(Team)
            Matches = int(Matches)
            Bat_Runs = int(Bat_Runs)
            Bat_Average = float(Bat_Average)
            Catches = int(Catches)
            Debut = datetime.strptime(Debut)
            tupla = cricket(Name,Team,Nationality,Matches,Bat_Runs,Bat_Average,Catches,Debut)
            datos.append(tupla)
        return(datos)